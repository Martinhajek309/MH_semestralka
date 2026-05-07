"""Benchmark point searches with no index, a tile index and GeoPandas sindex."""

from __future__ import annotations

import csv
import json
import random
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import geopandas as gpd
from shapely.geometry import box

from linear_search import search_points
from tile_index import TileIndex


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
RESULTS_DIR = PROJECT_ROOT / "results"
AREA_PATH = DATA_DIR / "olomoucky_kraj_5514.geojson"
AREA_NAME = "Olomoucky kraj"
DATASET_SIZES = (500, 1000, 5000)
QUERY_WINDOW_SIZES_M = (1000, 5000, 10000)
QUERY_COUNT = 1000
RANDOM_SEED = 20260507
TILE_SIZE_M = 1000

Point = tuple[float, float]
BBox = tuple[float, float, float, float]


@dataclass
class MethodResult:
    method: str
    index_build_seconds: float
    search_seconds: float
    total_found_points: int
    counts_by_query: list[int]

    @property
    def total_seconds(self) -> float:
        return self.index_build_seconds + self.search_seconds

    @property
    def average_found_points_per_query(self) -> float:
        return self.total_found_points / len(self.counts_by_query)


def load_geojson(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def crs_name(data: dict) -> str | None:
    crs = data.get("crs", {})
    properties = crs.get("properties", {})
    name = properties.get("name")
    return str(name).upper() if name else None


def load_points(path: Path) -> list[Point]:
    data = load_geojson(path)
    if crs_name(data) != "EPSG:5514":
        raise ValueError(f"{path} must use CRS EPSG:5514.")

    points = []
    for feature in data.get("features", []):
        geometry = feature.get("geometry", {})
        if geometry.get("type") != "Point":
            raise ValueError(f"{path} contains a non-Point geometry.")

        x, y = geometry.get("coordinates", [])[:2]
        points.append((float(x), float(y)))

    return points


def load_points_gdf(path: Path) -> gpd.GeoDataFrame:
    gdf = gpd.read_file(path)
    if gdf.crs is None:
        gdf = gdf.set_crs("EPSG:5514")
    else:
        gdf = gdf.to_crs("EPSG:5514")

    if not all(gdf.geometry.geom_type == "Point"):
        raise ValueError(f"{path} contains a non-Point geometry.")

    return gdf


def area_bbox(path: Path) -> BBox:
    data = load_geojson(path)
    if crs_name(data) != "EPSG:5514":
        raise ValueError(f"{path} must use CRS EPSG:5514.")

    coordinates: list[Point] = []

    def collect(values: object) -> None:
        if (
            isinstance(values, list)
            and len(values) >= 2
            and all(isinstance(item, (int, float)) for item in values[:2])
        ):
            coordinates.append((float(values[0]), float(values[1])))
            return

        if isinstance(values, list):
            for item in values:
                collect(item)

    for feature in data.get("features", []):
        collect(feature.get("geometry", {}).get("coordinates", []))
    if not coordinates:
        raise ValueError(f"{path} does not contain polygon coordinates.")

    xs = [point[0] for point in coordinates]
    ys = [point[1] for point in coordinates]
    return min(xs), min(ys), max(xs), max(ys)


def generate_queries(area: BBox, window_size_m: int, count: int) -> list[BBox]:
    rng = random.Random(RANDOM_SEED + window_size_m)
    min_x, min_y, max_x, max_y = area
    if max_x - min_x < window_size_m or max_y - min_y < window_size_m:
        raise ValueError(f"Window size {window_size_m} m is larger than area bbox.")

    queries = []
    for _ in range(count):
        x = rng.uniform(min_x, max_x - window_size_m)
        y = rng.uniform(min_y, max_y - window_size_m)
        queries.append((x, y, x + window_size_m, y + window_size_m))

    return queries


def time_call(callback: Callable[[], object]) -> tuple[object, float]:
    start = time.perf_counter()
    result = callback()
    return result, time.perf_counter() - start


def benchmark_linear(points: list[Point], queries: list[BBox]) -> MethodResult:
    counts = []
    start = time.perf_counter()
    for query in queries:
        counts.append(len(search_points(points, query)))
    search_seconds = time.perf_counter() - start

    return MethodResult(
        method="linear_search",
        index_build_seconds=0.0,
        search_seconds=search_seconds,
        total_found_points=sum(counts),
        counts_by_query=counts,
    )


def benchmark_tile(points: list[Point], queries: list[BBox]) -> MethodResult:
    index, index_build_seconds = time_call(lambda: TileIndex.build(points, TILE_SIZE_M))

    counts = []
    start = time.perf_counter()
    for query in queries:
        counts.append(len(index.search(query)))
    search_seconds = time.perf_counter() - start

    return MethodResult(
        method="tile_index",
        index_build_seconds=index_build_seconds,
        search_seconds=search_seconds,
        total_found_points=sum(counts),
        counts_by_query=counts,
    )


def benchmark_rtree(gdf: gpd.GeoDataFrame, queries: list[BBox]) -> MethodResult:
    spatial_index, index_build_seconds = time_call(lambda: gdf.sindex)

    counts = []
    start = time.perf_counter()
    for query in queries:
        min_x, min_y, max_x, max_y = query
        candidate_indices = spatial_index.query(box(min_x, min_y, max_x, max_y))
        candidates = gdf.iloc[candidate_indices]
        exact_matches = candidates[
            (candidates.geometry.x >= min_x)
            & (candidates.geometry.x <= max_x)
            & (candidates.geometry.y >= min_y)
            & (candidates.geometry.y <= max_y)
        ]
        counts.append(len(exact_matches))
    search_seconds = time.perf_counter() - start

    return MethodResult(
        method="rtree_index",
        index_build_seconds=index_build_seconds,
        search_seconds=search_seconds,
        total_found_points=sum(counts),
        counts_by_query=counts,
    )


def verify_results(results: list[MethodResult], queries: list[BBox]) -> None:
    reference = results[0]
    for result in results[1:]:
        if result.total_found_points != reference.total_found_points:
            for query_index, (reference_count, result_count) in enumerate(
                zip(reference.counts_by_query, result.counts_by_query),
                start=1,
            ):
                if reference_count != result_count:
                    raise ValueError(
                        f"Search results differ for query {query_index}: "
                        f"{reference.method}={reference_count}, "
                        f"{result.method}={result_count}, bbox={queries[query_index - 1]}"
                    )

            raise ValueError(
                f"Search totals differ: {reference.method}="
                f"{reference.total_found_points}, {result.method}="
                f"{result.total_found_points}"
            )


def result_row(
    dataset_size: int,
    window_size_m: int,
    result: MethodResult,
) -> dict[str, object]:
    tile_size = TILE_SIZE_M if result.method == "tile_index" else ""
    return {
        "area_name": AREA_NAME,
        "dataset_size": dataset_size,
        "query_count": QUERY_COUNT,
        "query_window_size_m": window_size_m,
        "method": result.method,
        "index_build_seconds": f"{result.index_build_seconds:.9f}",
        "search_seconds": f"{result.search_seconds:.9f}",
        "total_seconds": f"{result.total_seconds:.9f}",
        "total_found_points": result.total_found_points,
        "average_found_points_per_query": f"{result.average_found_points_per_query:.6f}",
        "tile_size_m": tile_size,
    }


def save_results(rows: list[dict[str, object]]) -> None:
    output_path = RESULTS_DIR / "benchmark_search.csv"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "area_name",
        "dataset_size",
        "query_count",
        "query_window_size_m",
        "method",
        "index_build_seconds",
        "search_seconds",
        "total_seconds",
        "total_found_points",
        "average_found_points_per_query",
        "tile_size_m",
    ]

    with output_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    area = area_bbox(AREA_PATH)
    queries_by_window = {
        window_size_m: generate_queries(area, window_size_m, QUERY_COUNT)
        for window_size_m in QUERY_WINDOW_SIZES_M
    }
    rows = []

    for dataset_size in DATASET_SIZES:
        points_path = DATA_DIR / f"random_points_{dataset_size}_olomoucky_kraj_5514.geojson"
        points = load_points(points_path)
        gdf = load_points_gdf(points_path)

        for window_size_m, queries in queries_by_window.items():
            results = [
                benchmark_linear(points, queries),
                benchmark_tile(points, queries),
                benchmark_rtree(gdf, queries),
            ]
            verify_results(results, queries)
            rows.extend(result_row(dataset_size, window_size_m, result) for result in results)

            totals = ", ".join(
                f"{result.method}={result.total_found_points}" for result in results
            )
            print(
                f"dataset={dataset_size}, window={window_size_m} m, "
                f"queries={QUERY_COUNT}: {totals}"
            )

    save_results(rows)
    print(f"Saved {RESULTS_DIR / 'benchmark_search.csv'}")


if __name__ == "__main__":
    main()

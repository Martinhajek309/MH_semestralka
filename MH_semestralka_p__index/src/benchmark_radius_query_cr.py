"""Benchmark radius queries over Czech Republic point datasets in EPSG:5514."""

from __future__ import annotations

import csv
import json
import math
import random
import time
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

import geopandas as gpd
import shapely
from shapely.geometry import Point as ShapelyPoint
from shapely.geometry import box


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
RESULTS_DIR = PROJECT_ROOT / "results"
AREA_PATH = DATA_DIR / "ceska_republika_5514.geojson"
AREA_NAME = "Ceska republika"
DATASET_SIZES = (5000, 10000, 50000)
RADII_M = (5000, 10000, 25000)
QUERY_COUNT = 1000
RANDOM_SEED = 20260508
TILE_SIZE_M = 5000

Point = tuple[float, float]
BBox = tuple[float, float, float, float]
Tile = tuple[int, int]


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


@dataclass
class RadiusTileIndex:
    tile_size: float
    tiles: dict[Tile, list[Point]]

    @classmethod
    def build(cls, points: list[Point], tile_size: float) -> "RadiusTileIndex":
        tiles: dict[Tile, list[Point]] = defaultdict(list)
        index = cls(tile_size=tile_size, tiles=tiles)
        for point in points:
            tiles[index.tile_for_point(point)].append(point)
        return index

    def tile_for_point(self, point: Point) -> Tile:
        x, y = point
        return math.floor(x / self.tile_size), math.floor(y / self.tile_size)

    def tiles_for_bbox(self, bbox: BBox) -> list[Tile]:
        min_x, min_y, max_x, max_y = bbox
        min_tile_x = math.floor(min_x / self.tile_size)
        min_tile_y = math.floor(min_y / self.tile_size)
        max_tile_x = math.floor(max_x / self.tile_size)
        max_tile_y = math.floor(max_y / self.tile_size)

        return [
            (tile_x, tile_y)
            for tile_x in range(min_tile_x, max_tile_x + 1)
            for tile_y in range(min_tile_y, max_tile_y + 1)
        ]

    def search_radius(self, query: Point, radius: float) -> list[Point]:
        x, y = query
        radius_squared = radius * radius
        bbox = (x - radius, y - radius, x + radius, y + radius)
        result = []

        for tile in self.tiles_for_bbox(bbox):
            for point_x, point_y in self.tiles.get(tile, []):
                dx = point_x - x
                dy = point_y - y
                if dx * dx + dy * dy <= radius_squared:
                    result.append((point_x, point_y))

        return result


def load_geojson(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def crs_name(data: dict[str, Any]) -> str | None:
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


def load_area_geometry(path: Path) -> Any:
    gdf = gpd.read_file(path)
    if gdf.crs is None:
        data = load_geojson(path)
        if crs_name(data) != "EPSG:5514":
            raise ValueError(f"{path} must use CRS EPSG:5514.")
        gdf = gdf.set_crs("EPSG:5514")
    else:
        gdf = gdf.to_crs("EPSG:5514")

    geometry = gdf.geometry.union_all()
    if geometry.is_empty:
        raise ValueError(f"{path} contains an empty geometry.")

    shapely.prepare(geometry)
    return geometry


def generate_query_points(area_geometry: Any) -> list[Point]:
    rng = random.Random(RANDOM_SEED)
    min_x, min_y, max_x, max_y = area_geometry.bounds
    queries: list[Point] = []

    while len(queries) < QUERY_COUNT:
        x = rng.uniform(min_x, max_x)
        y = rng.uniform(min_y, max_y)
        if shapely.contains(area_geometry, ShapelyPoint(x, y)):
            queries.append((x, y))

    return queries


def time_call(callback: Callable[[], object]) -> tuple[object, float]:
    start = time.perf_counter()
    result = callback()
    return result, time.perf_counter() - start


def benchmark_linear_radius(
    points: list[Point],
    queries: list[Point],
    radius: float,
) -> MethodResult:
    radius_squared = radius * radius
    counts = []
    start = time.perf_counter()

    for query_x, query_y in queries:
        count = 0
        for point_x, point_y in points:
            dx = point_x - query_x
            dy = point_y - query_y
            if dx * dx + dy * dy <= radius_squared:
                count += 1
        counts.append(count)

    search_seconds = time.perf_counter() - start
    return MethodResult(
        method="linear_search_radius",
        index_build_seconds=0.0,
        search_seconds=search_seconds,
        total_found_points=sum(counts),
        counts_by_query=counts,
    )


def benchmark_tile_radius(
    points: list[Point],
    queries: list[Point],
    radius: float,
) -> MethodResult:
    index, index_build_seconds = time_call(lambda: RadiusTileIndex.build(points, TILE_SIZE_M))

    counts = []
    start = time.perf_counter()
    for query in queries:
        counts.append(len(index.search_radius(query, radius)))
    search_seconds = time.perf_counter() - start

    return MethodResult(
        method="tile_index_radius",
        index_build_seconds=index_build_seconds,
        search_seconds=search_seconds,
        total_found_points=sum(counts),
        counts_by_query=counts,
    )


def benchmark_rtree_radius(
    gdf: gpd.GeoDataFrame,
    queries: list[Point],
    radius: float,
) -> MethodResult:
    spatial_index, index_build_seconds = time_call(lambda: gdf.sindex)
    radius_squared = radius * radius

    counts = []
    start = time.perf_counter()
    for query_x, query_y in queries:
        candidate_indices = spatial_index.query(
            box(query_x - radius, query_y - radius, query_x + radius, query_y + radius)
        )
        candidates = gdf.iloc[candidate_indices]
        dx = candidates.geometry.x - query_x
        dy = candidates.geometry.y - query_y
        exact_matches = candidates[(dx * dx + dy * dy) <= radius_squared]
        counts.append(len(exact_matches))

    search_seconds = time.perf_counter() - start
    return MethodResult(
        method="rtree_index_radius",
        index_build_seconds=index_build_seconds,
        search_seconds=search_seconds,
        total_found_points=sum(counts),
        counts_by_query=counts,
    )


def verify_results(
    dataset_size: int,
    radius: int,
    results: list[MethodResult],
) -> None:
    reference = results[0]
    for result in results[1:]:
        if result.total_found_points != reference.total_found_points:
            for query_index, (reference_count, result_count) in enumerate(
                zip(reference.counts_by_query, result.counts_by_query),
                start=1,
            ):
                if reference_count != result_count:
                    raise ValueError(
                        f"Radius query results differ: dataset_size={dataset_size}, "
                        f"radius_m={radius}, query_index={query_index}, "
                        f"{reference.method}={reference_count}, "
                        f"{result.method}={result_count}"
                    )

            raise ValueError(
                f"Radius query totals differ: dataset_size={dataset_size}, "
                f"radius_m={radius}, {reference.method}={reference.total_found_points}, "
                f"{result.method}={result.total_found_points}"
            )


def result_row(dataset_size: int, radius: int, result: MethodResult) -> dict[str, object]:
    tile_size = TILE_SIZE_M if result.method == "tile_index_radius" else ""
    return {
        "area_name": AREA_NAME,
        "dataset_size": dataset_size,
        "query_count": QUERY_COUNT,
        "radius_m": radius,
        "method": result.method,
        "index_build_seconds": f"{result.index_build_seconds:.9f}",
        "search_seconds": f"{result.search_seconds:.9f}",
        "total_seconds": f"{result.total_seconds:.9f}",
        "total_found_points": result.total_found_points,
        "average_found_points_per_query": f"{result.average_found_points_per_query:.6f}",
        "tile_size_m": tile_size,
    }


def save_results(rows: list[dict[str, object]]) -> None:
    output_path = RESULTS_DIR / "benchmark_radius_query_cr.csv"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "area_name",
        "dataset_size",
        "query_count",
        "radius_m",
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
    area_geometry = load_area_geometry(AREA_PATH)
    queries = generate_query_points(area_geometry)
    rows = []

    for dataset_size in DATASET_SIZES:
        points_path = DATA_DIR / f"random_points_{dataset_size}_cr_5514.geojson"
        points = load_points(points_path)
        gdf = load_points_gdf(points_path)

        for radius in RADII_M:
            results = [
                benchmark_linear_radius(points, queries, radius),
                benchmark_tile_radius(points, queries, radius),
                benchmark_rtree_radius(gdf, queries, radius),
            ]
            verify_results(dataset_size, radius, results)
            rows.extend(result_row(dataset_size, radius, result) for result in results)

            totals = ", ".join(
                f"{result.method}={result.total_found_points}" for result in results
            )
            print(
                f"dataset={dataset_size}, radius={radius} m, "
                f"queries={QUERY_COUNT}: {totals}"
            )

    save_results(rows)
    print(f"Saved {RESULTS_DIR / 'benchmark_radius_query_cr.csv'}")


if __name__ == "__main__":
    main()

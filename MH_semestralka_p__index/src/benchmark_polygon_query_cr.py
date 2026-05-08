"""Benchmark point-in-polygon queries for Czech regions in EPSG:5514."""

from __future__ import annotations

import csv
import json
import math
import ssl
import time
import urllib.parse
import urllib.request
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

import geopandas as gpd
import numpy as np
import shapely
from shapely.geometry import mapping


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
RESULTS_DIR = PROJECT_ROOT / "results"
REGIONS_4326 = DATA_DIR / "kraje_cr.geojson"
REGIONS_5514 = DATA_DIR / "kraje_cr_5514.geojson"
AREA_NAME = "Ceska republika"
SOURCE_NAME = "Ceska geologicka sluzba - Topografie/uzemni_identifikace, vrstva Kraje"
SOURCE_LAYER_URL = (
    "https://mapy.geology.cz/arcgis/rest/services/"
    "Topografie/uzemni_identifikace/MapServer/0/query"
)
SOURCE_LAYER_PAGE = (
    "https://mapy.geology.cz/arcgis/rest/services/"
    "Topografie/uzemni_identifikace/MapServer/0"
)
DATASET_SIZES = (5000, 10000, 50000)
TILE_SIZE_M = 5000
POLYGON_COUNT = 14

Point = tuple[float, float]
Tile = tuple[int, int]
BBox = tuple[float, float, float, float]


@dataclass
class MethodResult:
    method: str
    index_build_seconds: float
    search_seconds: float
    counts_by_kraj: dict[str, int]

    @property
    def total_seconds(self) -> float:
        return self.index_build_seconds + self.search_seconds

    @property
    def total_found_points(self) -> int:
        return sum(self.counts_by_kraj.values())

    @property
    def average_found_points_per_polygon(self) -> float:
        return self.total_found_points / len(self.counts_by_kraj)


@dataclass
class PolygonTileIndex:
    tile_size: float
    tiles: dict[Tile, list[Point]]

    @classmethod
    def build(cls, points: list[Point], tile_size: float) -> "PolygonTileIndex":
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

    def candidates_for_polygon(self, polygon: Any) -> list[Point]:
        candidates: list[Point] = []
        for tile in self.tiles_for_bbox(tuple(polygon.bounds)):
            candidates.extend(self.tiles.get(tile, []))
        return candidates


def fetch_json(url: str, params: dict[str, str]) -> dict[str, Any]:
    query = urllib.parse.urlencode(params)
    request = urllib.request.Request(
        f"{url}?{query}",
        headers={"User-Agent": "KGI-PRODA-2026 semestral project"},
    )
    ssl_context = ssl._create_unverified_context()
    with urllib.request.urlopen(request, timeout=60, context=ssl_context) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return json.loads(response.read().decode(charset))


def crs_name(data: dict[str, Any]) -> str | None:
    crs = data.get("crs", {})
    properties = crs.get("properties", {})
    name = properties.get("name")
    return str(name).upper() if name else None


def read_geojson_crs(path: Path) -> str | None:
    with path.open("r", encoding="utf-8") as file:
        return crs_name(json.load(file))


def load_geojson(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def candidate_region_files() -> list[Path]:
    ignored = {
        REGIONS_4326.name,
        REGIONS_5514.name,
        "ceska_republika.geojson",
        "ceska_republika_5514.geojson",
        "olomoucky_kraj.geojson",
        "olomoucky_kraj_5514.geojson",
    }
    return [
        path
        for path in DATA_DIR.glob("*.geojson")
        if path.name not in ignored and "random_points" not in path.name
    ]


def try_load_regions_from_file(path: Path) -> gpd.GeoDataFrame | None:
    try:
        gdf = gpd.read_file(path)
    except Exception:
        return None

    if len(gdf) != POLYGON_COUNT:
        return None

    polygon_types = {"Polygon", "MultiPolygon"}
    if not set(gdf.geometry.geom_type).issubset(polygon_types):
        return None

    if gdf.crs is None:
        file_crs = read_geojson_crs(path)
        if not file_crs:
            return None
        gdf = gdf.set_crs(file_crs)

    return gdf


def download_regions_4326() -> gpd.GeoDataFrame:
    data = fetch_json(
        SOURCE_LAYER_URL,
        {
            "where": "1=1",
            "outFields": "objectid,kod_nuts3,nazev_nuts",
            "returnGeometry": "true",
            "outSR": "4326",
            "f": "geojson",
        },
    )
    return gpd.GeoDataFrame.from_features(data["features"], crs="EPSG:4326")


def normalize_region_names(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    result = gdf.copy()
    name_candidates = ["kraj_name", "kraje", "nazev_nuts", "NAZEV_NUTS", "name", "nazev"]
    source_column = next((column for column in name_candidates if column in result.columns), None)
    if source_column is None:
        raise ValueError("Region layer does not contain a usable region-name column.")

    result["kraj_name"] = result[source_column].astype(str)
    result["kraje"] = result["kraj_name"]
    result["source"] = SOURCE_NAME
    return result[["kraj_name", "kraje", "source", "geometry"]].sort_values("kraj_name")


def feature_collection(gdf: gpd.GeoDataFrame, epsg: int) -> dict[str, Any]:
    features = []
    for _, row in gdf.iterrows():
        features.append(
            {
                "type": "Feature",
                "properties": {
                    "kraj_name": row["kraj_name"],
                    "kraje": row["kraje"],
                    "source": row["source"],
                },
                "geometry": mapping(row.geometry),
            }
        )

    return {
        "type": "FeatureCollection",
        "name": "kraje_cr" if epsg == 4326 else "kraje_cr_5514",
        "crs": {"type": "name", "properties": {"name": f"EPSG:{epsg}"}},
        "features": features,
    }


def save_regions(path: Path, gdf: gpd.GeoDataFrame, epsg: int) -> None:
    with path.open("w", encoding="utf-8") as file:
        json.dump(feature_collection(gdf.to_crs(f"EPSG:{epsg}"), epsg), file, ensure_ascii=False)
        file.write("\n")


def validate_regions(path: Path, expected_epsg: int) -> None:
    if not path.exists():
        raise FileNotFoundError(path)

    if read_geojson_crs(path) != f"EPSG:{expected_epsg}":
        raise ValueError(f"{path} must declare CRS EPSG:{expected_epsg}.")

    gdf = gpd.read_file(path)
    if len(gdf) != POLYGON_COUNT:
        raise ValueError(f"{path} contains {len(gdf)} regions, expected {POLYGON_COUNT}.")

    if "kraj_name" not in gdf.columns:
        raise ValueError(f"{path} does not contain kraj_name.")

    if not set(gdf.geometry.geom_type).issubset({"Polygon", "MultiPolygon"}):
        raise ValueError(f"{path} contains a non-polygon geometry.")

    if gdf.geometry.is_empty.any():
        raise ValueError(f"{path} contains an empty geometry.")


def prepare_regions() -> gpd.GeoDataFrame:
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if REGIONS_5514.exists():
        validate_regions(REGIONS_5514, 5514)
        return gpd.read_file(REGIONS_5514).to_crs("EPSG:5514")

    regions = None
    for path in candidate_region_files():
        regions = try_load_regions_from_file(path)
        if regions is not None:
            print(f"Using local region layer {path}")
            break

    if regions is None:
        regions = download_regions_4326()
        print(f"Downloaded {len(regions)} regions from {SOURCE_LAYER_PAGE}")

    regions = normalize_region_names(regions)
    save_regions(REGIONS_4326, regions, 4326)
    save_regions(REGIONS_5514, regions, 5514)
    validate_regions(REGIONS_4326, 4326)
    validate_regions(REGIONS_5514, 5514)
    return gpd.read_file(REGIONS_5514).to_crs("EPSG:5514")


def load_points(path: Path) -> tuple[list[Point], np.ndarray, np.ndarray]:
    data = load_geojson(path)
    if crs_name(data) != "EPSG:5514":
        raise ValueError(f"{path} must use CRS EPSG:5514.")

    points: list[Point] = []
    for feature in data.get("features", []):
        geometry = feature.get("geometry", {})
        if geometry.get("type") != "Point":
            raise ValueError(f"{path} contains a non-Point geometry.")
        x, y = geometry.get("coordinates", [])[:2]
        points.append((float(x), float(y)))

    xs = np.array([point[0] for point in points])
    ys = np.array([point[1] for point in points])
    return points, xs, ys


def load_points_gdf(path: Path) -> gpd.GeoDataFrame:
    gdf = gpd.read_file(path)
    if gdf.crs is None:
        gdf = gdf.set_crs("EPSG:5514")
    else:
        gdf = gdf.to_crs("EPSG:5514")
    return gdf


def time_call(callback: Callable[[], object]) -> tuple[object, float]:
    start = time.perf_counter()
    result = callback()
    return result, time.perf_counter() - start


def benchmark_linear_polygon(regions: gpd.GeoDataFrame, xs: np.ndarray, ys: np.ndarray) -> MethodResult:
    point_geometries = shapely.points(xs, ys)
    counts = {}
    start = time.perf_counter()

    for _, region in regions.iterrows():
        counts[region["kraj_name"]] = int(shapely.contains(region.geometry, point_geometries).sum())

    search_seconds = time.perf_counter() - start
    return MethodResult("linear_search_polygon", 0.0, search_seconds, counts)


def benchmark_tile_polygon(regions: gpd.GeoDataFrame, points: list[Point]) -> MethodResult:
    index, index_build_seconds = time_call(lambda: PolygonTileIndex.build(points, TILE_SIZE_M))
    counts = {}
    start = time.perf_counter()

    for _, region in regions.iterrows():
        candidates = index.candidates_for_polygon(region.geometry)
        if candidates:
            xs = np.array([point[0] for point in candidates])
            ys = np.array([point[1] for point in candidates])
            counts[region["kraj_name"]] = int(shapely.contains(region.geometry, shapely.points(xs, ys)).sum())
        else:
            counts[region["kraj_name"]] = 0

    search_seconds = time.perf_counter() - start
    return MethodResult("tile_index_polygon", index_build_seconds, search_seconds, counts)


def benchmark_rtree_polygon(regions: gpd.GeoDataFrame, gdf: gpd.GeoDataFrame) -> MethodResult:
    spatial_index, index_build_seconds = time_call(lambda: gdf.sindex)
    counts = {}
    start = time.perf_counter()

    for _, region in regions.iterrows():
        candidate_indices = spatial_index.query(region.geometry.envelope)
        candidates = gdf.iloc[candidate_indices]
        if len(candidates) == 0:
            counts[region["kraj_name"]] = 0
        else:
            counts[region["kraj_name"]] = int(shapely.contains(region.geometry, candidates.geometry.array).sum())

    search_seconds = time.perf_counter() - start
    return MethodResult("rtree_index_polygon", index_build_seconds, search_seconds, counts)


def verify_results(dataset_size: int, results: list[MethodResult]) -> None:
    for result in results:
        if result.total_found_points != dataset_size:
            raise ValueError(
                f"dataset_size={dataset_size}, method={result.method}, "
                f"total_found_points={result.total_found_points}, expected={dataset_size}"
            )

    reference = results[0]
    for result in results[1:]:
        for kraj_name, reference_count in reference.counts_by_kraj.items():
            result_count = result.counts_by_kraj[kraj_name]
            if result_count != reference_count:
                counts = {
                    method_result.method: method_result.counts_by_kraj[kraj_name]
                    for method_result in results
                }
                raise ValueError(
                    f"Polygon query results differ: dataset_size={dataset_size}, "
                    f"kraj_name={kraj_name}, counts={counts}"
                )


def summary_row(dataset_size: int, result: MethodResult) -> dict[str, object]:
    tile_size = TILE_SIZE_M if result.method == "tile_index_polygon" else ""
    return {
        "area_name": AREA_NAME,
        "dataset_size": dataset_size,
        "polygon_count": POLYGON_COUNT,
        "method": result.method,
        "index_build_seconds": f"{result.index_build_seconds:.9f}",
        "search_seconds": f"{result.search_seconds:.9f}",
        "total_seconds": f"{result.total_seconds:.9f}",
        "total_found_points": result.total_found_points,
        "average_found_points_per_polygon": f"{result.average_found_points_per_polygon:.6f}",
        "tile_size_m": tile_size,
    }


def save_summary(rows: list[dict[str, object]]) -> None:
    output_path = RESULTS_DIR / "benchmark_polygon_query_cr.csv"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "area_name",
        "dataset_size",
        "polygon_count",
        "method",
        "index_build_seconds",
        "search_seconds",
        "total_seconds",
        "total_found_points",
        "average_found_points_per_polygon",
        "tile_size_m",
    ]
    with output_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def save_details(rows: list[dict[str, object]]) -> None:
    output_path = RESULTS_DIR / "polygon_query_counts_by_kraj.csv"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["dataset_size", "method", "kraj_name", "found_points"]
    with output_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    regions = prepare_regions()
    summary_rows: list[dict[str, object]] = []
    detail_rows: list[dict[str, object]] = []

    for dataset_size in DATASET_SIZES:
        points_path = DATA_DIR / f"random_points_{dataset_size}_cr_5514.geojson"
        points, xs, ys = load_points(points_path)
        gdf = load_points_gdf(points_path)

        results = [
            benchmark_linear_polygon(regions, xs, ys),
            benchmark_tile_polygon(regions, points),
            benchmark_rtree_polygon(regions, gdf),
        ]
        verify_results(dataset_size, results)

        for result in results:
            summary_rows.append(summary_row(dataset_size, result))
            for kraj_name, found_points in result.counts_by_kraj.items():
                detail_rows.append(
                    {
                        "dataset_size": dataset_size,
                        "method": result.method,
                        "kraj_name": kraj_name,
                        "found_points": found_points,
                    }
                )

        totals = ", ".join(f"{result.method}={result.total_found_points}" for result in results)
        print(f"dataset={dataset_size}, polygons={POLYGON_COUNT}: {totals}")

    save_summary(summary_rows)
    save_details(detail_rows)
    print(f"Saved {RESULTS_DIR / 'benchmark_polygon_query_cr.csv'}")
    print(f"Saved {RESULTS_DIR / 'polygon_query_counts_by_kraj.csv'}")


if __name__ == "__main__":
    main()

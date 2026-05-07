"""Benchmark linear point search against a tile-based spatial index in EPSG:5514."""

from __future__ import annotations

import argparse
import csv
import json
import random
import time
from pathlib import Path

from linear_search import search_points
from tile_index import TileIndex


Point = tuple[float, float]
BBox = tuple[float, float, float, float]


def load_points(path: Path) -> list[Point]:
    with path.open("r", encoding="utf-8") as file:
        geojson = json.load(file)

    points = []
    for feature in geojson.get("features", []):
        geometry = feature.get("geometry", {})
        if geometry.get("type") != "Point":
            continue

        x, y = geometry["coordinates"][:2]
        points.append((float(x), float(y)))

    return points


def get_bbox(points: list[Point]) -> BBox:
    xs = [point[0] for point in points]
    ys = [point[1] for point in points]
    return min(xs), min(ys), max(xs), max(ys)


def random_query_bbox(area: BBox, width_ratio: float = 0.05) -> BBox:
    min_x, min_y, max_x, max_y = area
    width = (max_x - min_x) * width_ratio
    height = (max_y - min_y) * width_ratio
    x = random.uniform(min_x, max_x - width)
    y = random.uniform(min_y, max_y - height)
    return x, y, x + width, y + height


def benchmark_linear(points: list[Point], queries: list[BBox]) -> float:
    start = time.perf_counter()
    for query in queries:
        search_points(points, query)
    return time.perf_counter() - start


def benchmark_tile_index(points: list[Point], queries: list[BBox], tile_size: float) -> float:
    index = TileIndex.build(points, tile_size)

    start = time.perf_counter()
    for query in queries:
        index.search(query)
    return time.perf_counter() - start


def save_results(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["method", "point_count", "query_count", "tile_size", "elapsed_seconds"]

    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--points",
        type=Path,
        default=Path("data/random_points_olomoucky_kraj.geojson"),
    )
    parser.add_argument("--output", type=Path, default=Path("results/benchmark_results.csv"))
    parser.add_argument("--queries", type=int, default=1_000)
    parser.add_argument("--tile-size", type=float, default=5_000.0)
    args = parser.parse_args()

    points = load_points(args.points)
    if not points:
        raise ValueError("Point dataset is empty. Generate or add input points first.")

    queries = [random_query_bbox(get_bbox(points)) for _ in range(args.queries)]

    rows = [
        {
            "method": "linear",
            "point_count": len(points),
            "query_count": len(queries),
            "tile_size": "",
            "elapsed_seconds": benchmark_linear(points, queries),
        },
        {
            "method": "tile_index",
            "point_count": len(points),
            "query_count": len(queries),
            "tile_size": args.tile_size,
            "elapsed_seconds": benchmark_tile_index(points, queries, args.tile_size),
        },
    ]
    save_results(args.output, rows)


if __name__ == "__main__":
    main()

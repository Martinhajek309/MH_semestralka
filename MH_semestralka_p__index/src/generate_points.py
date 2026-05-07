"""Generate random points inside the study area in EPSG:5514.

The script expects a GeoJSON polygon of the Olomouc Region and creates a
GeoJSON file with random points inside its bounding box. Coordinates are
handled in EPSG:5514, so distances and tile sizes are in meters. The exact
point-in-polygon filtering can be extended later with shapely/geopandas.
"""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path


def load_geojson(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def get_bbox(geojson: dict) -> tuple[float, float, float, float]:
    coordinates: list[tuple[float, float]] = []

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

    collect(geojson.get("features", []))

    if not coordinates:
        raise ValueError("Input GeoJSON does not contain any coordinates.")

    xs = [point[0] for point in coordinates]
    ys = [point[1] for point in coordinates]
    return min(xs), min(ys), max(xs), max(ys)


def generate_points(bbox: tuple[float, float, float, float], count: int) -> dict:
    min_x, min_y, max_x, max_y = bbox
    features = []

    for point_id in range(count):
        x = random.uniform(min_x, max_x)
        y = random.uniform(min_y, max_y)
        features.append(
            {
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [x, y]},
                "properties": {"id": point_id},
            }
        )

    return {"type": "FeatureCollection", "features": features}


def save_geojson(path: Path, geojson: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(geojson, file, ensure_ascii=False, indent=2)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=Path("data/olomoucky_kraj_5514.geojson"))
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/random_points_olomoucky_kraj.geojson"),
    )
    parser.add_argument("--count", type=int, default=10_000)
    args = parser.parse_args()

    area = load_geojson(args.input)
    points = generate_points(get_bbox(area), args.count)
    save_geojson(args.output, points)


if __name__ == "__main__":
    main()

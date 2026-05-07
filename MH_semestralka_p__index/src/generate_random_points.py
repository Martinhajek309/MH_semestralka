"""Generate reproducible random point layers inside the Olomouc Region.

The working CRS is EPSG:5514, so generated coordinates are in meters.
"""

from __future__ import annotations

import json
import random
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
REGION_5514 = DATA_DIR / "olomoucky_kraj_5514.geojson"
REGION_4326 = DATA_DIR / "olomoucky_kraj.geojson"
DATASET_SIZES = (500, 1000, 5000)
RANDOM_SEED = 20260507

Point = tuple[float, float]
Ring = list[Point]
Polygon = list[Ring]
MultiPolygon = list[Polygon]
BBox = tuple[float, float, float, float]


def load_geojson(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_geojson(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
        file.write("\n")


def crs_name(data: dict[str, Any]) -> str | None:
    crs = data.get("crs", {})
    properties = crs.get("properties", {})
    name = properties.get("name")
    return str(name).upper() if name else None


def ensure_epsg_5514(region: dict[str, Any]) -> dict[str, Any]:
    region["crs"] = {"type": "name", "properties": {"name": "EPSG:5514"}}
    for feature in region.get("features", []):
        feature.setdefault("properties", {})["epsg"] = 5514
    return region


def transform_4326_to_5514(region: dict[str, Any]) -> dict[str, Any]:
    try:
        from pyproj import Transformer
    except ImportError as exc:
        raise RuntimeError(
            "data/olomoucky_kraj_5514.geojson does not exist. Install pyproj "
            "with `pip install -r requirements.txt` to transform the EPSG:4326 file."
        ) from exc

    transformer = Transformer.from_crs("EPSG:4326", "EPSG:5514", always_xy=True)

    def transform_coordinates(values: Any) -> Any:
        if (
            isinstance(values, list)
            and len(values) >= 2
            and all(isinstance(item, (int, float)) for item in values[:2])
        ):
            x, y = transformer.transform(float(values[0]), float(values[1]))
            return [x, y]

        if isinstance(values, list):
            return [transform_coordinates(item) for item in values]

        return values

    transformed = json.loads(json.dumps(region))
    for feature in transformed.get("features", []):
        geometry = feature.get("geometry", {})
        geometry["coordinates"] = transform_coordinates(geometry.get("coordinates", []))

    return ensure_epsg_5514(transformed)


def load_region_5514() -> dict[str, Any]:
    if REGION_5514.exists():
        return ensure_epsg_5514(load_geojson(REGION_5514))

    if not REGION_4326.exists():
        raise FileNotFoundError(
            "Missing data/olomoucky_kraj_5514.geojson and data/olomoucky_kraj.geojson."
        )

    region = transform_4326_to_5514(load_geojson(REGION_4326))
    save_geojson(REGION_5514, region)
    return region


def geometry_to_multipolygon(geometry: dict[str, Any]) -> MultiPolygon:
    geometry_type = geometry.get("type")
    coordinates = geometry.get("coordinates", [])

    if geometry_type == "Polygon":
        return [
            [[(float(x), float(y)) for x, y, *_ in ring] for ring in coordinates]
        ]

    if geometry_type == "MultiPolygon":
        return [
            [[(float(x), float(y)) for x, y, *_ in ring] for ring in polygon]
            for polygon in coordinates
        ]

    raise ValueError(f"Unsupported region geometry type: {geometry_type}")


def region_multipolygon(region: dict[str, Any]) -> MultiPolygon:
    multipolygon: MultiPolygon = []
    for feature in region.get("features", []):
        multipolygon.extend(geometry_to_multipolygon(feature.get("geometry", {})))

    if not multipolygon:
        raise ValueError("Region GeoJSON does not contain any polygon geometry.")

    return multipolygon


def bbox_for_multipolygon(multipolygon: MultiPolygon) -> BBox:
    points = [point for polygon in multipolygon for ring in polygon for point in ring]
    xs = [point[0] for point in points]
    ys = [point[1] for point in points]
    return min(xs), min(ys), max(xs), max(ys)


def ring_bbox(ring: Ring) -> BBox:
    xs = [point[0] for point in ring]
    ys = [point[1] for point in ring]
    return min(xs), min(ys), max(xs), max(ys)


def point_in_bbox(point: Point, bbox: BBox) -> bool:
    x, y = point
    min_x, min_y, max_x, max_y = bbox
    return min_x <= x <= max_x and min_y <= y <= max_y


def point_in_ring(point: Point, ring: Ring) -> bool:
    x, y = point
    inside = False
    previous_x, previous_y = ring[-1]

    for current_x, current_y in ring:
        crosses_y = (current_y > y) != (previous_y > y)
        if crosses_y:
            intersection_x = (
                (previous_x - current_x) * (y - current_y)
                / (previous_y - current_y)
                + current_x
            )
            if x < intersection_x:
                inside = not inside

        previous_x, previous_y = current_x, current_y

    return inside


def point_in_polygon(point: Point, polygon: Polygon, ring_bboxes: list[BBox]) -> bool:
    exterior = polygon[0]
    if not point_in_bbox(point, ring_bboxes[0]):
        return False

    if not point_in_ring(point, exterior):
        return False

    for hole, hole_bbox in zip(polygon[1:], ring_bboxes[1:]):
        if point_in_bbox(point, hole_bbox) and point_in_ring(point, hole):
            return False

    return True


def prepare_polygon_bboxes(multipolygon: MultiPolygon) -> list[list[BBox]]:
    return [[ring_bbox(ring) for ring in polygon] for polygon in multipolygon]


def point_in_multipolygon(
    point: Point,
    multipolygon: MultiPolygon,
    polygon_bboxes: list[list[BBox]],
) -> bool:
    return any(
        point_in_polygon(point, polygon, ring_bboxes)
        for polygon, ring_bboxes in zip(multipolygon, polygon_bboxes)
    )


def generate_points(
    count: int,
    multipolygon: MultiPolygon,
    rng: random.Random,
) -> tuple[list[Point], int]:
    bbox = bbox_for_multipolygon(multipolygon)
    polygon_bboxes = prepare_polygon_bboxes(multipolygon)
    min_x, min_y, max_x, max_y = bbox
    points: list[Point] = []
    attempts = 0

    while len(points) < count:
        attempts += 1
        point = (rng.uniform(min_x, max_x), rng.uniform(min_y, max_y))
        if point_in_multipolygon(point, multipolygon, polygon_bboxes):
            points.append(point)

    return points, attempts


def points_to_geojson(points: list[Point], dataset_size: int) -> dict[str, Any]:
    return {
        "type": "FeatureCollection",
        "name": f"random_points_{dataset_size}_olomoucky_kraj_5514",
        "crs": {"type": "name", "properties": {"name": "EPSG:5514"}},
        "features": [
            {
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [x, y]},
                "properties": {
                    "id": point_id,
                    "dataset_size": dataset_size,
                    "x": x,
                    "y": y,
                },
            }
            for point_id, (x, y) in enumerate(points, start=1)
        ],
    }


def validate_points(
    path: Path,
    expected_count: int,
    multipolygon: MultiPolygon,
) -> None:
    data = load_geojson(path)
    if crs_name(data) != "EPSG:5514":
        raise ValueError(f"{path} does not declare CRS EPSG:5514.")

    features = data.get("features", [])
    if len(features) != expected_count:
        raise ValueError(f"{path} contains {len(features)} points, expected {expected_count}.")

    polygon_bboxes = prepare_polygon_bboxes(multipolygon)
    for feature in features:
        geometry = feature.get("geometry", {})
        if geometry.get("type") != "Point":
            raise ValueError(f"{path} contains a non-Point geometry.")

        x, y = geometry.get("coordinates", [])[:2]
        point = (float(x), float(y))
        if not point_in_multipolygon(point, multipolygon, polygon_bboxes):
            raise ValueError(f"{path} contains a point outside the region polygon.")


def main() -> None:
    region = load_region_5514()
    if crs_name(region) != "EPSG:5514":
        raise ValueError("Region polygon must use CRS EPSG:5514.")

    multipolygon = region_multipolygon(region)
    rng = random.Random(RANDOM_SEED)

    for dataset_size in DATASET_SIZES:
        points, attempts = generate_points(dataset_size, multipolygon, rng)
        output_path = DATA_DIR / f"random_points_{dataset_size}_olomoucky_kraj_5514.geojson"
        save_geojson(output_path, points_to_geojson(points, dataset_size))
        validate_points(output_path, dataset_size, multipolygon)

        print(
            f"{output_path.name}: {dataset_size} points, "
            f"CRS EPSG:5514, attempts {attempts}"
        )


if __name__ == "__main__":
    main()

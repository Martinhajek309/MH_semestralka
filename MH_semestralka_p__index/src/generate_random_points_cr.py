"""Generate random point layers inside the Czech Republic polygon in EPSG:5514."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import geopandas as gpd
import numpy as np
import shapely
from shapely.geometry import mapping


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
COUNTRY_5514 = DATA_DIR / "ceska_republika_5514.geojson"
COUNTRY_4326 = DATA_DIR / "ceska_republika.geojson"
AREA_NAME = "Ceska republika"
DATASET_SIZES = (5000, 10000, 50000)
RANDOM_SEED = 20260507
BATCH_SIZE = 25_000


def crs_name(data: dict[str, Any]) -> str | None:
    crs = data.get("crs", {})
    properties = crs.get("properties", {})
    name = properties.get("name")
    return str(name).upper() if name else None


def read_geojson_crs(path: Path) -> str | None:
    with path.open("r", encoding="utf-8") as file:
        return crs_name(json.load(file))


def load_country_polygon() -> gpd.GeoDataFrame:
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if COUNTRY_5514.exists():
        gdf = gpd.read_file(COUNTRY_5514)
        file_crs = read_geojson_crs(COUNTRY_5514)
        if gdf.crs is None and file_crs:
            gdf = gdf.set_crs(file_crs)
        return gdf.to_crs("EPSG:5514")

    if not COUNTRY_4326.exists():
        raise FileNotFoundError(
            "Missing data/ceska_republika_5514.geojson and data/ceska_republika.geojson."
        )

    gdf = gpd.read_file(COUNTRY_4326)
    file_crs = read_geojson_crs(COUNTRY_4326)
    if gdf.crs is None:
        gdf = gdf.set_crs(file_crs or "EPSG:4326")

    country_5514 = gdf.to_crs("EPSG:5514")
    save_feature_collection(COUNTRY_5514, country_5514.geometry.iloc[0], [])
    return country_5514


def save_feature_collection(
    path: Path,
    geometry: Any | None,
    features: list[dict[str, Any]],
) -> None:
    if geometry is not None and not features:
        features = [
            {
                "type": "Feature",
                "properties": {"area_name": AREA_NAME},
                "geometry": mapping(geometry),
            }
        ]

    data = {
        "type": "FeatureCollection",
        "name": path.stem,
        "crs": {"type": "name", "properties": {"name": "EPSG:5514"}},
        "features": features,
    }
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, separators=(",", ":"))
        file.write("\n")


def country_geometry(country: gpd.GeoDataFrame) -> Any:
    if len(country) != 1:
        geometry = country.geometry.union_all()
    else:
        geometry = country.geometry.iloc[0]

    if geometry.is_empty:
        raise ValueError("Czech Republic polygon is empty.")

    if geometry.geom_type not in {"Polygon", "MultiPolygon"}:
        raise ValueError(f"Unsupported country geometry type: {geometry.geom_type}")

    return geometry


def generate_points(
    geometry: Any,
    dataset_size: int,
    rng: np.random.Generator,
) -> tuple[np.ndarray, np.ndarray, int]:
    min_x, min_y, max_x, max_y = geometry.bounds
    accepted_x: list[np.ndarray] = []
    accepted_y: list[np.ndarray] = []
    accepted_count = 0
    attempts = 0

    while accepted_count < dataset_size:
        remaining = dataset_size - accepted_count
        batch_size = max(BATCH_SIZE, remaining * 3)
        xs = rng.uniform(min_x, max_x, batch_size)
        ys = rng.uniform(min_y, max_y, batch_size)
        candidates = shapely.points(xs, ys)
        mask = shapely.contains(geometry, candidates)
        selected_indices = np.flatnonzero(mask)

        if len(selected_indices) == 0:
            attempts += batch_size
            continue

        take = min(remaining, len(selected_indices))
        attempts += int(selected_indices[take - 1]) + 1 if take < len(selected_indices) else batch_size
        accepted_x.append(xs[selected_indices[:take]])
        accepted_y.append(ys[selected_indices[:take]])
        accepted_count += take

    return np.concatenate(accepted_x), np.concatenate(accepted_y), attempts


def points_to_features(xs: np.ndarray, ys: np.ndarray, dataset_size: int) -> list[dict[str, Any]]:
    features = []
    for point_id, (x, y) in enumerate(zip(xs, ys), start=1):
        point_x = float(x)
        point_y = float(y)
        features.append(
            {
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [point_x, point_y]},
                "properties": {
                    "id": point_id,
                    "dataset_size": dataset_size,
                    "area_name": AREA_NAME,
                    "x": point_x,
                    "y": point_y,
                },
            }
        )
    return features


def save_points(path: Path, xs: np.ndarray, ys: np.ndarray, dataset_size: int) -> None:
    save_feature_collection(path, None, points_to_features(xs, ys, dataset_size))


def validate_points(path: Path, dataset_size: int, geometry: Any) -> None:
    if not path.exists():
        raise FileNotFoundError(path)

    data = json.loads(path.read_text(encoding="utf-8"))
    data_crs = crs_name(data)
    if data_crs != "EPSG:5514":
        raise ValueError(f"{path} declares CRS {data_crs}, expected EPSG:5514.")

    features = data.get("features", [])
    if len(features) != dataset_size:
        raise ValueError(f"{path} contains {len(features)} points, expected {dataset_size}.")

    xs = np.empty(dataset_size)
    ys = np.empty(dataset_size)
    for index, feature in enumerate(features):
        geometry_data = feature.get("geometry", {})
        if geometry_data.get("type") != "Point":
            raise ValueError(f"{path} contains a non-Point geometry.")

        properties = feature.get("properties", {})
        if properties.get("dataset_size") != dataset_size:
            raise ValueError(f"{path} contains an incorrect dataset_size attribute.")

        if properties.get("area_name") != AREA_NAME:
            raise ValueError(f"{path} contains an incorrect area_name attribute.")

        x, y = geometry_data.get("coordinates", [])[:2]
        xs[index] = float(x)
        ys[index] = float(y)

    points_inside = shapely.contains(geometry, shapely.points(xs, ys))
    if not bool(points_inside.all()):
        outside_count = int((~points_inside).sum())
        raise ValueError(f"{path} contains {outside_count} points outside the country polygon.")


def main() -> None:
    country = load_country_polygon()
    geometry = country_geometry(country)
    shapely.prepare(geometry)

    for dataset_size in DATASET_SIZES:
        rng = np.random.default_rng(RANDOM_SEED + dataset_size)
        xs, ys, attempts = generate_points(geometry, dataset_size, rng)
        output_path = DATA_DIR / f"random_points_{dataset_size}_cr_5514.geojson"
        save_points(output_path, xs, ys, dataset_size)
        validate_points(output_path, dataset_size, geometry)

        success_rate = dataset_size / attempts * 100
        print(
            f"{output_path.name}: {dataset_size} points, CRS EPSG:5514, "
            f"attempts {attempts}, success {success_rate:.2f}%"
        )


if __name__ == "__main__":
    main()

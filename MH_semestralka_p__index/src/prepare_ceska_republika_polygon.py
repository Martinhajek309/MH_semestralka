"""Prepare Czech Republic polygons for supplementary spatial-index benchmarks."""

from __future__ import annotations

import json
import ssl
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

import geopandas as gpd
from shapely.geometry import mapping
from shapely.ops import unary_union


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_4326 = DATA_DIR / "ceska_republika.geojson"
OUTPUT_5514 = DATA_DIR / "ceska_republika_5514.geojson"
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
EXPECTED_AREA_M2 = 78_871_000_000
AREA_TOLERANCE_M2 = 2_500_000_000


def fetch_json(url: str, params: dict[str, str]) -> dict[str, Any]:
    query = urllib.parse.urlencode(params)
    request = urllib.request.Request(
        f"{url}?{query}",
        headers={"User-Agent": "KGI-PRODA-2026 semestral project"},
    )

    # The public CGS ArcGIS endpoint currently fails Python's strict certificate
    # validation, so this script keeps the trusted source explicit and repeatable.
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


def candidate_region_files() -> list[Path]:
    ignored = {
        OUTPUT_4326.name,
        OUTPUT_5514.name,
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

    if len(gdf) < 13:
        return None

    polygon_types = {"Polygon", "MultiPolygon"}
    if not set(gdf.geometry.geom_type).issubset(polygon_types):
        return None

    if gdf.crs is None:
        file_crs = read_geojson_crs(path)
        if file_crs:
            gdf = gdf.set_crs(file_crs)
        else:
            return None

    gdf["source"] = f"Local file {path.name}"
    return gdf


def load_local_regions() -> gpd.GeoDataFrame | None:
    for path in candidate_region_files():
        gdf = try_load_regions_from_file(path)
        if gdf is not None:
            print(f"Using local region layer {path}")
            return gdf
    return None


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
    gdf = gpd.GeoDataFrame.from_features(data["features"], crs="EPSG:4326")
    gdf["source"] = SOURCE_NAME
    print(f"Downloaded {len(gdf)} regions from {SOURCE_LAYER_PAGE}")
    return gdf


def load_regions() -> gpd.GeoDataFrame:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    local_regions = load_local_regions()
    if local_regions is not None:
        return local_regions
    return download_regions_4326()


def dissolve_country(regions: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    regions_5514 = regions.to_crs("EPSG:5514")
    geometry = unary_union(regions_5514.geometry)

    return gpd.GeoDataFrame(
        [{"area_name": AREA_NAME, "source": SOURCE_NAME, "geometry": geometry}],
        crs="EPSG:5514",
    )


def feature_collection(gdf: gpd.GeoDataFrame, epsg: int) -> dict[str, Any]:
    if len(gdf) != 1:
        raise ValueError("Output GeoDataFrame must contain exactly one feature.")

    feature = gdf.iloc[0]
    return {
        "type": "FeatureCollection",
        "name": "ceska_republika" if epsg == 4326 else "ceska_republika_5514",
        "crs": {"type": "name", "properties": {"name": f"EPSG:{epsg}"}},
        "features": [
            {
                "type": "Feature",
                "properties": {
                    "area_name": AREA_NAME,
                    "source": feature["source"],
                },
                "geometry": mapping(feature.geometry),
            }
        ],
    }


def save_geojson(path: Path, gdf: gpd.GeoDataFrame, epsg: int) -> None:
    data = feature_collection(gdf.to_crs(f"EPSG:{epsg}"), epsg)
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
        file.write("\n")


def count_vertices(geometry: Any) -> int:
    if geometry.geom_type == "Polygon":
        return sum(len(ring.coords) for ring in [geometry.exterior, *geometry.interiors])
    if geometry.geom_type == "MultiPolygon":
        return sum(count_vertices(part) for part in geometry.geoms)
    return 0


def validate_output(path: Path, expected_epsg: int) -> None:
    if not path.exists():
        raise FileNotFoundError(path)

    gdf = gpd.read_file(path)
    data_crs = read_geojson_crs(path)
    if data_crs != f"EPSG:{expected_epsg}":
        raise ValueError(f"{path} declares {data_crs}, expected EPSG:{expected_epsg}.")

    if len(gdf) != 1:
        raise ValueError(f"{path} contains {len(gdf)} features, expected 1.")

    geometry = gdf.geometry.iloc[0]
    if geometry.is_empty:
        raise ValueError(f"{path} contains an empty geometry.")

    if geometry.geom_type not in {"Polygon", "MultiPolygon"}:
        raise ValueError(f"{path} geometry is {geometry.geom_type}, expected Polygon/MultiPolygon.")

    if count_vertices(geometry) <= 5:
        raise ValueError(f"{path} looks like a bbox because it has too few vertices.")

    envelope_area = geometry.envelope.area
    if envelope_area > 0 and geometry.area / envelope_area > 0.95:
        raise ValueError(f"{path} looks like a bbox because it almost fills its envelope.")

    if expected_epsg == 5514:
        area = geometry.area
        min_area = EXPECTED_AREA_M2 - AREA_TOLERANCE_M2
        max_area = EXPECTED_AREA_M2 + AREA_TOLERANCE_M2
        if not min_area <= area <= max_area:
            raise ValueError(
                f"{path} area is {area:.0f} m2, expected approximately "
                f"{EXPECTED_AREA_M2:.0f} m2."
            )


def validate_outputs() -> None:
    validate_output(OUTPUT_4326, 4326)
    validate_output(OUTPUT_5514, 5514)


def main() -> None:
    regions = load_regions()
    if len(regions) < 13:
        raise ValueError(f"Expected a layer of Czech regions, got {len(regions)} features.")

    country_5514 = dissolve_country(regions)
    save_geojson(OUTPUT_4326, country_5514, 4326)
    save_geojson(OUTPUT_5514, country_5514, 5514)
    validate_outputs()

    area_km2 = country_5514.geometry.iloc[0].area / 1_000_000
    print(f"Saved {OUTPUT_4326.relative_to(PROJECT_ROOT)} in EPSG:4326")
    print(f"Saved {OUTPUT_5514.relative_to(PROJECT_ROOT)} in EPSG:5514")
    print(f"Features: 1, geometry: {country_5514.geometry.iloc[0].geom_type}")
    print(f"Area in EPSG:5514: {area_km2:.2f} km2")


if __name__ == "__main__":
    main()

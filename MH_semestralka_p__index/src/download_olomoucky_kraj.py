"""Download the Olomouc Region polygon in EPSG:4326 and EPSG:5514."""

from __future__ import annotations

import json
import ssl
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"

SOURCE_LAYER_URL = (
    "https://mapy.geology.cz/arcgis/rest/services/"
    "Topografie/uzemni_identifikace/MapServer/0/query"
)
SOURCE_NAME = "Ceska geologicka sluzba - Topografie/uzemni_identifikace, vrstva Kraje"
SOURCE_LAYER_PAGE = (
    "https://mapy.geology.cz/arcgis/rest/services/"
    "Topografie/uzemni_identifikace/MapServer/0"
)
OLOMOUC_NUTS3 = "CZ071"


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


def fetch_geojson_4326() -> dict[str, Any]:
    return fetch_json(
        SOURCE_LAYER_URL,
        {
            "where": f"kod_nuts3 = '{OLOMOUC_NUTS3}'",
            "outFields": "objectid,kod_nuts3,nazev_nuts",
            "returnGeometry": "true",
            "outSR": "4326",
            "f": "geojson",
        },
    )


def fetch_arcgis_json_5514() -> dict[str, Any]:
    return fetch_json(
        SOURCE_LAYER_URL,
        {
            "where": f"kod_nuts3 = '{OLOMOUC_NUTS3}'",
            "outFields": "objectid,kod_nuts3,nazev_nuts",
            "returnGeometry": "true",
            "outSR": "5514",
            "f": "json",
        },
    )


def arcgis_polygon_to_geojson(feature: dict[str, Any]) -> dict[str, Any]:
    rings = feature["geometry"]["rings"]
    return {
        "type": "Feature",
        "properties": {
            **feature.get("attributes", {}),
            "source": SOURCE_NAME,
            "source_url": SOURCE_LAYER_PAGE,
            "epsg": 5514,
        },
        "geometry": {
            "type": "Polygon",
            "coordinates": rings,
        },
    }


def arcgis_json_to_geojson_5514(data: dict[str, Any]) -> dict[str, Any]:
    features = data.get("features", [])
    if len(features) != 1:
        raise ValueError(f"Expected exactly one Olomouc Region feature, got {len(features)}.")

    return {
        "type": "FeatureCollection",
        "name": "olomoucky_kraj_5514",
        "crs": {
            "type": "name",
            "properties": {"name": "EPSG:5514"},
        },
        "features": [arcgis_polygon_to_geojson(features[0])],
    }


def normalize_geojson_4326(data: dict[str, Any]) -> dict[str, Any]:
    features = data.get("features", [])
    if len(features) != 1:
        raise ValueError(f"Expected exactly one Olomouc Region feature, got {len(features)}.")

    feature = features[0]
    feature["properties"] = {
        **feature.get("properties", {}),
        "source": SOURCE_NAME,
        "source_url": SOURCE_LAYER_PAGE,
        "epsg": 4326,
    }
    data["name"] = "olomoucky_kraj"
    return data


def save_geojson(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
        file.write("\n")


def main() -> None:
    geojson_4326 = normalize_geojson_4326(fetch_geojson_4326())
    geojson_5514 = arcgis_json_to_geojson_5514(fetch_arcgis_json_5514())

    save_geojson(DATA_DIR / "olomoucky_kraj.geojson", geojson_4326)
    save_geojson(DATA_DIR / "olomoucky_kraj_5514.geojson", geojson_5514)

    print("Saved data/olomoucky_kraj.geojson in EPSG:4326")
    print("Saved data/olomoucky_kraj_5514.geojson in EPSG:5514")


if __name__ == "__main__":
    main()

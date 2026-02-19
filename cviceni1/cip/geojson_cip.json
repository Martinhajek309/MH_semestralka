import json
from pathlib import Path
import folium

points = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {"name": "Point A", "popup": "Olomouc - Horní náměstí"},
            "geometry": {"type": "Point", "coordinates": [17.2509, 49.5938]},
        },
        {
            "type": "Feature",
            "properties": {"name": "Point B", "popup": "Olomouc - Univerzita"},
            "geometry": {"type": "Point", "coordinates": [17.2480, 49.5970]},
        },
    ],
}


def main():
    out_dir = Path(__file__).parent
    geojson_path = out_dir / "points.geojson"
    with open(geojson_path, "w", encoding="utf-8") as f:
        json.dump(points, f, ensure_ascii=False, indent=2)

    avg_lat = sum(f["geometry"]["coordinates"][1] for f in points["features"]) / len(points["features"]) 
    avg_lon = sum(f["geometry"]["coordinates"][0] for f in points["features"]) / len(points["features"])

    m = folium.Map(location=[avg_lat, avg_lon], zoom_start=14, tiles="OpenStreetMap")

    for feat in points["features"]:
        lon, lat = feat["geometry"]["coordinates"]
        popup = feat["properties"].get("popup", feat["properties"].get("name", ""))
        folium.Marker([lat, lon], popup=popup).add_to(m)

    folium.GeoJson(points, name="points").add_to(m)
    m.save(out_dir / "map.html")

    print("GeoJSON saved to:", geojson_path)
    print("Map saved to:", out_dir / "map.html")


if __name__ == "__main__":
    main()

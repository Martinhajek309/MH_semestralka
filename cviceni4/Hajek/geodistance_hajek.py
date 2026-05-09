def vypocitej_vzdalenost_od_rovniku(
    sirka: float,
    jednotka: str = "km",
    zaokrouhlit: bool = False
) -> float:
    vzdalenost = abs(sirka) * 111.32

    if jednotka == "mi":
        vzdalenost = vzdalenost * 0.621371

    if zaokrouhlit:
        vzdalenost = round(vzdalenost)

    return vzdalenost


sirka_mest = [0, 15, 30, 45, 60]

for sirka in sirka_mest:
    vzdalenost_km = vypocitej_vzdalenost_od_rovniku(sirka)
    print(f"Město na šířce {sirka}° je {vzdalenost_km} km od rovníku.")

    vzdalenost_mi = vypocitej_vzdalenost_od_rovniku(sirka, jednotka="mi")
    print(f"Město na šířce {sirka}° je {vzdalenost_mi} mi od rovníku.")

    vzdalenost_km_zaokr = vypocitej_vzdalenost_od_rovniku(sirka, zaokrouhlit=True)
    print(f"Město na šířce {sirka}° je {vzdalenost_km_zaokr} km od rovníku.")

def vypocitej_vzdalenost_od_rovniku(
    sirka: float,
    jednotka: str = "km",
    zaokrouhlit: bool = False
) -> float:
    
    vzdalenost = abs(sirka) * 111.32

    if jednotka == "mi":
        vzdalenost = vzdalenost * 0.621371

    if zaokrouhlit:
        vzdalenost = round(vzdalenost)

    return vzdalenost


def vytvor_geojson_bod(nazev: str, lat: float, lon: float) -> str:
    
    vzdalenost = vypocitej_vzdalenost_od_rovniku(lat)

    geojson = f"""{{
  "type": "Feature",
  "properties": {{
    "nazev": "{nazev}",
    "vzdalenost_od_rovniku": {vzdalenost}
  }},
  "geometry": {{
    "type": "Point",
    "coordinates": [{lon}, {lat}]
  }}
}}"""
    return geojson
geojson_text = vytvor_geojson_bod("Praha", 50.0755, 14.4378)

with open("cviceni4/hajek/misto.geojson", "w", encoding="utf-8") as soubor:
    soubor.write(geojson_text)

print("GeoJSON soubor byl vytvořen.")
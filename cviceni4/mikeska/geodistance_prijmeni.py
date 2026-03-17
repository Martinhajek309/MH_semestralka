

def vypocitej_vzdalenost_od_rovniku(sirka: float, jednotka: str = "km", zaokrouhlit: bool = True) -> float:
    """
    Vypočítá vzdálenost od rovníku pro danou zeměpisnou šířku. 
    Parameters:
    -----------
    sirka : float
        Zeměpisná šířka ve stupních
    jednotka : str
        Jednotka vzdálenosti - "km" (kilometr) nebo "míle" (výchozí: "km")
    zaokrouhlit : bool
        Určuje, zda zaokrouhlit výsledek na celé číslo (výchozí: True)
    Returns:
    --------
    float
        Vzdálenost od rovníku v zadané jednotce
    """
    KM_NA_STUPEN = 111.32
    KM_NA_MILI = 0.621371
    
    vzdalenost = abs(sirka) * KM_NA_STUPEN
    
    if jednotka == "míle":
        vzdalenost *= KM_NA_MILI
    
    if zaokrouhlit:
        vzdalenost = round(vzdalenost)
    
    return vzdalenost

def vytvor_geojson_bod(nazev: str, lat: float, lon: float) -> str:
    """
    Vytvoří GeoJSON bod s informacemi o místě a jeho vzdálenosti od rovníku.
    Parameters:
    -----------
    nazev : str
        Název místa
    lat : float
        Zeměpisná šířka ve stupních (latitude)
    lon : float
        Zeměpisná délka ve stupních (longitude)
    Returns:
    --------
    str
        Validní GeoJSON bod ve formátu FeatureCollection s atributy nazev a vzdalenost_od_rovniku
    """
    import json 
    # Vypočítej vzdálenost od rovníku
    vzdalenost = vypocitej_vzdalenost_od_rovniku(lat, jednotka="km", zaokrouhlit=False)
    # Vytvoř GeoJSON bod
    geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {
                    "nazev": nazev,
                    "vzdalenost_od_rovniku": round(vzdalenost, 2)
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [lon, lat]
                }
            }
        ]
    }
    
    return json.dumps(geojson, indent=2, ensure_ascii=False)


sirky = [0, 1234.4, 30.43434, 45.2 , 60.5, 90]

print("=== Vzdálenosti v kilometrech ===")
for sirka in sirky:
    vzdalenost = vypocitej_vzdalenost_od_rovniku(sirka, jednotka="km")
    print(f"Město na šířce {sirka}° je {vzdalenost} km od rovníku.")


# Část A: GeoJSON bod
print("\n=== Vytvoření GeoJSON bodu ===")
geojson_prag = vytvor_geojson_bod("Praha", 50.0755, 14.4378)
print(geojson_prag)

# Uložení do souboru v současném adresáři
import os
soubor_cesta = os.path.join(os.path.dirname(__file__), "misto_mikeska.geojson")
with open(soubor_cesta, "w", encoding="utf-8") as f:
    f.write(geojson_prag)
print(f"\nGeoJSON bod byl uložen do souboru '{soubor_cesta}'")


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


# Vytvoření více GeoJSON souborů z listu krajských měst
print("\n=== Vytvoření GeoJSON souborů pro krajská města ===")
krajska_mesta = [
    {"nazev": "Praha", "lat": 50.0755, "lon": 14.4378},
    {"nazev": "Brno", "lat": 49.1922, "lon": 16.6113},
    {"nazev": "Plzeň", "lat": 49.7384, "lon": 13.3736},
    {"nazev": "Liberec", "lat": 50.7671, "lon": 15.0521},
    {"nazev": "Ústí nad Labem", "lat": 50.6625, "lon": 14.0327},
    {"nazev": "Hradec Králové", "lat": 50.2087, "lon": 15.8326},
    {"nazev": "Pardubice", "lat": 50.0374, "lon": 15.7739},
    {"nazev": "Jihlava", "lat": 49.3959, "lon": 15.5898},
    {"nazev": "Bruntál", "lat": 49.9839, "lon": 17.4695},
    {"nazev": "Ostrava", "lat": 49.8353, "lon": 18.2845},
]

for mesto in krajska_mesta:
    geojson_mesto = vytvor_geojson_bod(mesto["nazev"], mesto["lat"], mesto["lon"])
    
    # Vytvoření názvu souboru
    nazev_souboru = f"misto_{mesto['nazev'].lower()}.geojson"
    soubor_cesta = os.path.join(os.path.dirname(__file__), nazev_souboru)
    
    # Uložení do souboru
    with open(soubor_cesta, "w", encoding="utf-8") as f:
        f.write(geojson_mesto)
    
    print(f"✓ {mesto['nazev']} -> {nazev_souboru}")
import json

def vypocitej_vzdalenost_od_rovniku(
    sirka: float, 
    jednotka: str = "km", 
    zaokrouhlit: bool = False
) -> float:
    """Vypočítá přibližnou vzdálenost bodu od rovníku na základě zeměpisné šířky.""" 
    km_za_stupen = 111.32
    vzdalenost = abs(sirka) * km_za_stupen
    
    if jednotka == "mi":
        vzdalenost *= 0.621371
    
    if zaokrouhlit:
        return float(round(vzdalenost))
    
    return vzdalenost

def vytvor_geojson_bod(nazev: str, lat: float, lon: float) -> str:
    """Vytvoří GeoJSON prvek Point včetně vypočtené vzdálenosti od rovníku.""" 
   
    vzdalenost = vypocitej_vzdalenost_od_rovniku(lat, zaokrouhlit=True)
    
    geojson_data = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [lon, lat] 
        },
        "properties": {
            "nazev": nazev,
            "vzdalenost_od_rovniku_km": vzdalenost
        }
    }
    
    return json.dumps(geojson_data, indent=4, ensure_ascii=False)


seznam_sirek = [49.5938, 50.0755, 48.2082, 15.5000] 
for s in seznam_sirek:
    vzd = vypocitej_vzdalenost_od_rovniku(s, zaokrouhlit=True)
    print(f"Zeměpisná šířka {s}° je vzdálena {vzd} km od rovníku.")

mesto_nazev = "Olomouc"
mesto_lat = 49.5938
mesto_lon = 17.2509

geojson_vystup = vytvor_geojson_bod(mesto_nazev, mesto_lat, mesto_lon)

nazev_souboru = "misto_koutnik.geojson"
with open(nazev_souboru, "w", encoding="utf-8") as f:
    f.write(geojson_vystup)

print(f"Hotovo! Soubor '{nazev_souboru}' byl vytvořen.")

###############################################################################
# Oprava funkcí
###############################################################################

"""
Funkce_1:
- Co dělá: Převádí číselnou hodnotu mezi kilometry a mílemi podle parametru 'smer'.
- Problémy: 
    1. Chybí ošetření stavu, kdy uživatel zadá jiný řetězec než 'km_to_mi' nebo 'mi_to_km'. 
       V takovém případě funkce vrátí None, což může způsobit chybu v další části kódu.
    3. Používá dva samostatné 'if'. Lepší je struktura if-elif-else.
"""

def prevod(hodnota: float, smer: str) -> float:
    """Opravená verze funkce 1 s ošetřením neplatných vstupů."""
    if smer == "km_to_mi":
        return hodnota * 0.621371
    elif smer == "mi_to_km":
        return hodnota * 1.60934
    else:
        # Vyvolání chyby při špatném parametru 'smer'
        raise ValueError("Chyba: Směr musí být 'km_to_mi' nebo 'mi_to_km'!")


"""
Funkce 1:
- Co dělá: Přidá souřadnice (lat, lon) do seznamu a vypíše aktuální počet bodů.
- Problémy:
    1. Pracuje s globální proměnnou 'souradnice', což snižuje znovupoužitelnost kódu 
       a ztěžuje hledání chyb.
    2. GeoJSON a většina GIS knihoven vyžadují pořadí [lon, lat], funkce ukládá [lat, lon].
    3. Funkce postrádá return, takže upravený seznam nelze snadno předat dál.
"""

def pridej_bod_opraveny(lat: float, lon: float, seznam_bodu: list = None) -> list:
    """Opravená verze funkce 2, která je nezávislá na globálním prostoru."""
    if seznam_bodu is None:
        seznam_bodu = []
    
    # Ukládáme jako [longitude, latitude] pro kompatibilitu s GIS standardy
    seznam_bodu.append([lon, lat])
    
    print(f"Přidán bod: {lat}, {lon}")
    print(f"Celkem bodů v seznamu: {len(seznam_bodu)}")
    
    return seznam_bodu

###############################################################################
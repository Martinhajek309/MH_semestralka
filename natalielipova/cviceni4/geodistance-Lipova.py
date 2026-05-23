def vypocitej_vzdalenost_od_rovniku(sirka):
    vzdalenost = sirka * 111.32
    return vzdalenost

sirky = [0, 15, 30, 45, 60]

for sirka in sirky:
    vzdalenost = vypocitej_vzdalenost_od_rovniku(sirka)
    print(f"Město na šířce {sirka}° je {vzdalenost} km od rovníku.")

    def vypocitej_vzdalenost_od_rovniku(sirka: float, jednotka: str = "km", zaokrouhlit: bool = False) -> float:
    # Základní výpočet v km
        vzdalenost = sirka * 111.32
    
    # Přepočet na míle
        if jednotka == "mi":
            vzdalenost = vzdalenost * 0.621371
        
    # Zaokrouhlení
        if zaokrouhlit:
            vzdalenost = round(vzdalenost) 
        return vzdalenost


sirky = [0, 15, 30, 45, 60]

# Cyklus pro výpis různých kombinací
for s in sirky:
    # Příklad: výpočet v mílích se zaokrouhlením
    vysledek = vypocitej_vzdalenost_od_rovniku(s, jednotka="mi", zaokrouhlit=True)
    print(f"Město na šířce {s}° je {vysledek} mi od rovníku.")

import json

def vypocitej_vzdalenost_od_rovniku(sirka: float, jednotka: str = "km", zaokrouhlit: bool = False) -> float:
    """Vypočítá vzdálenost od rovníku."""
    vzdalenost = sirka * 111.32
    if jednotka == "mi":
        vzdalenost *= 0.621371
    if zaokrouhlit:
        vzdalenost = round(vzdalenost)
    return vzdalenost

def vytvor_geojson_bod(nazev: str, lat: float, lon: float) -> str:
    """Vytvoří validní GeoJSON string."""
    vzdal = vypocitej_vzdalenost_od_rovniku(lat)
    data = {
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [lon, lat]},
        "properties": {"nazev": nazev, "vzdalenost_od_rovniku": vzdal}
    }
    return json.dumps(data)

# 1. Spuštění výpočtu pro GeoJSON
moje_misto = vytvor_geojson_bod("Olomouc", 49.59, 17.25)

# 2. Uložení do souboru (vytvoří soubor misto_lipova.geojson)
with open("misto_lipova.geojson", "w") as f:
    f.write(moje_misto)

# 3. Kontrolní výpis pro tebe
sirky = [0, 15, 30, 45, 60]
for s in sirky:
    v = vypocitej_vzdalenost_od_rovniku(s)
    print(f"Město na šířce {s}° je {v} km od rovníku.")

# --- část B ---

# Funkce 1: Převádí vzdálenosti. 
# Problém: Chybí ošetření neplatného směru (vrátila by None).
def prevod(hodnota: float, smer: str) -> float:
    if smer == "km_to_mi":
        return hodnota * 0.621371
    elif smer == "mi_to_km":
        return hodnota * 1.60934
    else:
        # Oprava: Přidána pojistka pro neznámý směr
        print("Chyba: Neznámý směr převodu!")
        return 0.0

# Funkce 2: Přidává body do seznamu.
# Problém: Používá globální proměnnou (souradnice), což je riskantní.
# Také postrádá return, takže data jen vypíše, ale nevrátí pro další práci.
def pridej_bod(lat: float, lon: float, seznam_bodu: list) -> list:
    # Oprava: Seznam předáváme jako parametr, aby funkce byla "čistá"
    seznam_bodu.append([lat, lon])
    print(f"Přidán bod: {lat}, {lon}")
    print(f"Celkem bodů: {len(seznam_bodu)}")
    return seznam_bodu


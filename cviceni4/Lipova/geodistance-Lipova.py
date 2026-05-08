import json

def vypocitej_vzdalenost_od_rovniku(sirka: float, jednotka: str = "km", zaokrouhlit: bool = False) -> float:

    vzdalenost = sirka * 111.32
    
    if jednotka == "mi":
        vzdalenost *= 0.621371
        
    if zaokrouhlit:
        vzdalenost = round(vzdalenost)
        
    return vzdalenost

def vytvor_geojson_bod(nazev: str, lat: float, lon: float) -> str:
    
    vzdal = vypocitej_vzdalenost_od_rovniku(lat)
    data = {
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [lon, lat]},
        "properties": {"nazev": nazev, "vzdalenost_od_rovniku": vzdal}
    }
    return json.dumps(data)

def prevod(hodnota: float, smer: str) -> float:
   
    if smer == "km_to_mi":
        return hodnota * 0.621371
    elif smer == "mi_to_km":
        return hodnota * 1.60934
    else:
        print("Chyba: Neznámý směr převodu!")
        return 0.0

def pridej_bod(lat: float, lon: float, seznam_bodu: list) -> list:
    
    seznam_bodu.append([lat, lon])
    print(f"Přidán bod: {lat}, {lon}")
    return seznam_bodu


sirky = [0, 15, 30, 45, 60]

# Výpis základních vzdáleností v km
for s in sirky:
    v = vypocitej_vzdalenost_od_rovniku(s)
    print(f"Město na šířce {s}° je {v} km od rovníku.")

# Výpis vzdáleností v mílích se zaokrouhlením
for s in sirky:
    v_mi = vypocitej_vzdalenost_od_rovniku(s, jednotka="mi", zaokrouhlit=True)
    print(f"Město na šířce {s}° je {v_mi} mi od rovníku (zaokrouhleno).")

# Vytvoření a uložení GeoJSON souboru
moje_misto_json = vytvor_geojson_bod("Olomouc", 49.59, 17.25)
with open("misto_lipova.geojson", "w") as f:
    f.write(moje_misto_json)

# Ukázka práce se seznamem bodů
body = []
body = pridej_bod(49.59, 17.25, body)
body = pridej_bod(50.08, 14.43, body)
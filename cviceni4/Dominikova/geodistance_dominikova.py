
def vypocitej_vzdalenost_od_rovniku(sirka: float, jednotka: str = "km", zaokrouhlit: bool = False) -> float:
    vzdalenost = sirka * 111.32
    
    if jednotka == "míle":
        vzdalenost = vzdalenost * 0.621371
    
    if zaokrouhlit == True:
        vzdalenost = round(vzdalenost)
        
    return vzdalenost
"""
    Vypočítá vzdálenost zeměpisné šířky od rovníku
    
    - sirka: Zeměpisná šířka ve stupních 
    - jednotka: kilometry nebo míle
    - zaokrouhlit: Pokud je True, vrátí celé číslo
    
    Vrací:
    - Vzdálenost 
"""

sirky = [0, 15, 30, 45, 60]

for s in sirky:
    vysl = vypocitej_vzdalenost_od_rovniku(s, jednotka="km", zaokrouhlit=True)
    print(f"Město na šířce {s}° je {vysl} km od rovníku.")
vysl_mile = vypocitej_vzdalenost_od_rovniku(45, jednotka="míle", zaokrouhlit=False)
print(f"Město na šířce 45° je {vysl_mile} míle od rovníku.")





def vytvor_geojson_bod(nazev: str, lat: float, lon: float) -> str:
    """
    Vytvoří GeoJSON pro jeden bod s informací o vzdálenosti od rovníku
    """
    vzdalenost = vypocitej_vzdalenost_od_rovniku(lat, zaokrouhlit=True)
    
    geojson = f"""{{
  "type": "Feature",
  "geometry": {{
    "type": "Point",
    "coordinates": [{lon}, {lat}]
  }},
  "properties": {{
    "nazev": "{nazev}",
    "vzdalenost_od_rovniku_km": {vzdalenost}
  }}
}}"""
    return geojson

geojson_data = vytvor_geojson_bod("Praha", 50.08, 14.43)

with open("misto_prijmeni.geojson", "w", encoding="utf-8") as soubor:
    soubor.write(geojson_data)

print("Soubor 'misto_prijmeni.geojson' byl vytvořen.")

# Funkce 1:
# Převádí jednotky mezi kilometry a mílemi

def prevod(hodnota, smer):
    if smer == "km_to_mi":
        return hodnota * 0.621371
    if smer == "mi_to_km":
        return hodnota * 1.60934 

print(prevod(10, "km_to_mi"))


# Funkce 2:
# Přidává souřadnice bodu do seznamu a vypisuje info do konzole

souradnice = []

def pridej_bod(lat, lon):
    souradnice.append([lat, lon])
    print(f"Přidán bod: {lat}, {lon}")
    print(f"Celkem bodů: {len(souradnice)}")
 
print(pridej_bod(50,50))






# ------------------------------------------------
# ÚKOL 1 + 2: Výpočet vzdálenosti od rovníku
# ------------------------------------------------

def vypocitej_vzdalenost_od_rovniku(
    sirka: float,
    jednotka: str = "km",
    zaokrouhlit: bool = False
) -> float:
    """
    Vypočítá vzdálenost bodu od rovníku na základě zeměpisné šířky.

    Parametry:
    sirka (float) – zeměpisná šířka ve stupních
    jednotka (str) – jednotka výsledku ("km" nebo "mile")
    zaokrouhlit (bool) – pokud True, výsledek se zaokrouhlí

    Návratová hodnota:
    float – vzdálenost od rovníku v požadované jednotce
    """

    vzdalenost = abs(sirka) * 111.32

    if jednotka == "mile":
        vzdalenost = vzdalenost * 0.621371

    if zaokrouhlit:
        vzdalenost = round(vzdalenost)

    return vzdalenost


# seznam zeměpisných šířek
sirky = [0, 15, 30, 45, 60]

# výpočet vzdáleností
for sirka in sirky:

    vzdalenost_km = vypocitej_vzdalenost_od_rovniku(sirka)
    print(f"Město na šířce {sirka}° je {vzdalenost_km:.2f} km od rovníku.")

    vzdalenost_mile = vypocitej_vzdalenost_od_rovniku(sirka, jednotka="mile")
    print(f"Město na šířce {sirka}° je {vzdalenost_mile:.2f} mile od rovníku.")

    vzdalenost_zaokr = vypocitej_vzdalenost_od_rovniku(sirka, zaokrouhlit=True)
    print(f"Město na šířce {sirka}° je {vzdalenost_zaokr} km od rovníku.")

    print()


# ------------------------------------------------
# ÚKOL 3A: GeoJSON bod
# ------------------------------------------------

def vytvor_geojson_bod(nazev: str, lat: float, lon: float) -> str:
    """
    Vytvoří GeoJSON bod s atributem názvu a vzdálenosti od rovníku.

    Parametry:
    nazev (str) – název místa
    lat (float) – zeměpisná šířka
    lon (float) – zeměpisná délka

    Návratová hodnota:
    str – GeoJSON objekt jako text
    """

    vzdalenost = vypocitej_vzdalenost_od_rovniku(lat)

    geojson = f"""
{{
  "type": "Feature",
  "properties": {{
    "nazev": "{nazev}",
    "vzdalenost_od_rovniku": {vzdalenost}
  }},
  "geometry": {{
    "type": "Point",
    "coordinates": [{lon}, {lat}]
  }}
}}
"""

    return geojson


# vytvoření GeoJSON bodu pro Karvinou
geojson_data = vytvor_geojson_bod("Karviná", 49.854, 18.542)


# uložení souboru do správné složky
with open("cviceni4/Hrbacek/misto_hrbacek.geojson", "w", encoding="utf-8") as soubor:
    soubor.write(geojson_data)

print("GeoJSON byl uložen do cviceni4/Hrbacek/misto_hrbacek.geojson")


# ------------------------------------------------
# ÚKOL 3B: Čtení a oprava kódu
# ------------------------------------------------

# Funkce převádí vzdálenost mezi kilometry a mílemi.
# Problém původní verze:
# - pokud je zadán jiný směr než "km_to_mi" nebo "mi_to_km",
#   funkce nic nevrátí (vrátí None)
# - chyběly type hints

def prevod(hodnota: float, smer: str) -> float:
    if smer == "km_to_mi":
        return hodnota * 0.621371
    elif smer == "mi_to_km":
        return hodnota * 1.60934
    else:
        raise ValueError("Neplatný směr převodu")


# ------------------------------------------------

# Původní funkce používala globální proměnnou 'souradnice',
# což není dobrá praxe. Lepší je předat seznam jako parametr.

def pridej_bod(souradnice: list, lat: float, lon: float) -> None:
    souradnice.append([lat, lon])
    print(f"Přidán bod: {lat}, {lon}")
    print(f"Celkem bodů: {len(souradnice)}")
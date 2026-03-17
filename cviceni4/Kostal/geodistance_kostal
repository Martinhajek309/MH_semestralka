def vypocitej_vzdalenost_od_rovniku(
    sirka: float, jednotka: str = "km", zaokrouhlit: bool = False
) -> float:
    """
    Vypočítá vzdálenost od rovníku podle zeměpisné šířky.

    Parametry:
        sirka (float): Zeměpisná šířka ve stupních.
        jednotka (str): Jednotka výsledku - "km" nebo "mile".
        zaokrouhlit (bool): Určuje, zda se má výsledek zaokrouhlit.

    Návratová hodnota:
        float: Vzdálenost od rovníku v požadované jednotce.
    """
    vzdalenost_km = abs(sirka) * 111.32

    if jednotka == "km":
        vzdalenost = vzdalenost_km
    elif jednotka == "mile":
        vzdalenost = vzdalenost_km * 0.621371
    else:
        raise ValueError("Neplatná jednotka. Použij 'km' nebo 'mile'.")

    if zaokrouhlit:
        vzdalenost = round(vzdalenost)

    return vzdalenost


def vytvor_geojson_bod(nazev: str, lat: float, lon: float) -> str:
    """
    Vytvoří GeoJSON bod s názvem a vzdáleností od rovníku.

    Parametry:
        nazev (str): Název bodu.
        lat (float): Zeměpisná šířka.
        lon (float): Zeměpisná délka.

    Návratová hodnota:
        str: Textový řetězec obsahující validní GeoJSON bod.
    """
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


sirky = [0, 15, 30, 45, 60]

for sirka in sirky:
    vzdalenost1 = vypocitej_vzdalenost_od_rovniku(sirka)
    print(f"Město na šířce {sirka}° je {vzdalenost1} km od rovníku.")

    vzdalenost2 = vypocitej_vzdalenost_od_rovniku(sirka, "mile")
    print(f"Město na šířce {sirka}° je {vzdalenost2} mile od rovníku.")

    vzdalenost3 = vypocitej_vzdalenost_od_rovniku(sirka, "km", True)
    print(f"Město na šířce {sirka}° je {vzdalenost3} km od rovníku.")


geojson_bod = vytvor_geojson_bod("Olomouc", 49.5938, 17.2509)

with open("misto_prijmeni.geojson", "w", encoding="utf-8") as soubor:
    soubor.write(geojson_bod)


# Funkce 1:
# Co dělá:
# Převádí vzdálenost mezi kilometry a mílemi.
#
# Problém:
# Původní funkce neřešila neplatný směr převodu.
# Oprava: přidáno ošetření chybného vstupu.


def prevod(hodnota: float, smer: str) -> float:
    """
    Převede vzdálenost mezi kilometry a mílemi.

    Parametry:
        hodnota (float): Hodnota k převodu.
        smer (str): Směr převodu - "km_to_mi" nebo "mi_to_km".

    Návratová hodnota:
        float: Převedená hodnota.
    """
    if smer == "km_to_mi":
        return hodnota * 0.621371
    elif smer == "mi_to_km":
        return hodnota * 1.60934
    else:
        raise ValueError("Neplatný směr převodu.")


# Funkce 2:
# Co dělá:
# Přidává bod do seznamu souřadnic a vypisuje informace o bodu.
#
# Problém:
# Původní funkce používala globální proměnnou.
# Oprava: seznam souřadnic se předává jako parametr.


def pridej_bod(souradnice: list, lat: float, lon: float) -> None:
    """
    Přidá bod do seznamu souřadnic.

    Parametry:
        souradnice (list): Seznam bodů.
        lat (float): Zeměpisná šířka.
        lon (float): Zeměpisná délka.
    """
    souradnice.append([lat, lon])
    print(f"Přidán bod: {lat}, {lon}")
    print(f"Celkem bodů: {len(souradnice)}")


seznam_souradnic = []
pridej_bod(seznam_souradnic, 49.5938, 17.2509)
def vypocitej_vzdalenost_od_rovniku(
    sirka: float,
    jednotka: str = "km",
    zaokrouhlit: bool = False
) -> float:
    """
    Vypočítá vzdálenost od rovníku na základě zeměpisné šířky.

    Args:
        sirka (float): Zeměpisná šířka ve stupních.
        jednotka (str): Jednotka výstupu ("km" nebo "mile").
        zaokrouhlit (bool): Zda se má výsledek zaokrouhlit.

    Returns:
        float: Vzdálenost od rovníku v dané jednotce.
    """

    vzdalenost = abs(sirka) * 111.32

    if jednotka == "mile":
        vzdalenost *= 0.621371

    if zaokrouhlit:
        vzdalenost = round(vzdalenost)

    return vzdalenost


def vytvor_geojson_bod(
    nazev: str,
    lat: float,
    lon: float
) -> str:
    """
    Vytvoří GeoJSON bod s informací o vzdálenosti od rovníku.

    Args:
        nazev (str): Název místa.
        lat (float): Zeměpisná šířka.
        lon (float): Zeměpisná délka.

    Returns:
        str: GeoJSON reprezentace bodu.
    """

    vzdalenost = vypocitej_vzdalenost_od_rovniku(lat)

    geojson = f"""
{{
  "type": "Feature",
  "geometry": {{
    "type": "Point",
    "coordinates": [{lon}, {lat}]
  }},
  "properties": {{
    "nazev": "{nazev}",
    "vzdalenost_od_rovniku": {vzdalenost}
  }}
}}
"""
    return geojson


sirky = [0, 15, 30, 45, 60]

for sirka in sirky:
    for jednotka in ["km", "mile"]:
        for zaokrouhlit in [False, True]:
            vzdalenost = vypocitej_vzdalenost_od_rovniku(
                sirka, jednotka, zaokrouhlit
            )
            print(f"Město na šířce {sirka}° je {vzdalenost} {jednotka} od rovníku.")


geojson_data = vytvor_geojson_bod("Olomouc", 49.5938, 17.2509)

with open("misto_Tobola.geojson", "w", encoding="utf-8") as f:
    f.write(geojson_data)



def prevod(hodnota: float, smer: str) -> float:
    """
    Převádí hodnotu mezi kilometry a mílemi.

    Args:
        hodnota (float): Hodnota k převodu.
        smer (str): Směr převodu ("km_to_mi" nebo "mi_to_km").

    Returns:
        float: Přepočtená hodnota.
    """
    if smer == "km_to_mi":
        return hodnota * 0.621371
    elif smer == "mi_to_km":
        return hodnota * 1.60934
    else:
        raise ValueError("Neplatný směr převodu")


def pridej_bod(souradnice: list, lat: float, lon: float) -> None:
    """
    Přidá bod do seznamu souřadnic a vypíše informace.

    Args:
        souradnice (list): Seznam souřadnic.
        lat (float): Zeměpisná šířka.
        lon (float): Zeměpisná délka.
    """
    souradnice.append([lat, lon])
    print(f"Přidán bod: {lat}, {lon}")
    print(f"Celkem bodů: {len(souradnice)}")
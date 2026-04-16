import json
from pathlib import Path


def vypocitej_vzdalenost_od_rovniku(
    sirka: float,
    jednotka: str = "km",
    zaokrouhlit: bool = False
) -> float:
    """
    Vypočítá vzdálenost místa od rovníku na základě zeměpisné šířky.

    Parametry:
        sirka (float): Zeměpisná šířka ve stupních.
        jednotka (str, volitelné): Jednotka výsledku, "km" nebo "mi".
            Výchozí hodnota je "km".
        zaokrouhlit (bool, volitelné): Určuje, zda se má výsledek
            zaokrouhlit na celé číslo. Výchozí hodnota je False.

    Návratová hodnota:
        float: Vzdálenost od rovníku v zadané jednotce.
    """
    vzdalenost = abs(sirka) * 111.32

    if jednotka == "km":
        vysledek = vzdalenost
    elif jednotka == "mi":
        vysledek = vzdalenost * 0.621371
    else:
        raise ValueError("Neplatná jednotka. Použij 'km' nebo 'mi'.")

    if zaokrouhlit:
        vysledek = round(vysledek)

    return float(vysledek)


def vytvor_geojson_bod(nazev: str, lat: float, lon: float) -> str:
    """
    Vytvoří validní GeoJSON FeatureCollection s jedním bodem
    a atributy 'nazev' a 'vzdalenost_od_rovniku'.

    Parametry:
        nazev (str): Název bodu.
        lat (float): Zeměpisná šířka bodu.
        lon (float): Zeměpisná délka bodu.

    Návratová hodnota:
        str: Textový řetězec ve formátu GeoJSON.
    """
    geojson_data = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {
                    "nazev": nazev,
                    "vzdalenost_od_rovniku": vypocitej_vzdalenost_od_rovniku(lat)
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [lon, lat]
                }
            }
        ]
    }

    return json.dumps(geojson_data, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    # Úkol 1 + Úkol 2
    sirky = [0, 15, 30, 45, 60]
    kombinace = [
        ("km", False),
        ("mi", False),
        ("km", True),
        ("mi", True),
    ]

    for sirka in sirky:
        for jednotka, zaokrouhlit in kombinace:
            vzdalenost = vypocitej_vzdalenost_od_rovniku(
                sirka,
                jednotka=jednotka,
                zaokrouhlit=zaokrouhlit
            )

            if zaokrouhlit:
                print(f"Město na šířce {sirka}° je {vzdalenost:.0f} {jednotka} od rovníku.")
            else:
                print(f"Město na šířce {sirka}° je {vzdalenost:.2f} {jednotka} od rovníku.")

    # Úkol 3A
    geojson_text = vytvor_geojson_bod("Olomouc", 49.5938, 17.2509)

    cilova_slozka = Path(__file__).parent
    vystupni_soubor = cilova_slozka / "misto_cech.geojson"

    with open(vystupni_soubor, "w", encoding="utf-8") as soubor:
        soubor.write(geojson_text)

    print(f"\nSoubor '{vystupni_soubor.name}' byl úspěšně vytvořen.")

# Funkce 1:
# Co dělá: Převádí zadanou hodnotu mezi kilometry a mílemi podle směru převodu.
# Má nějaký problém? Ano. Nemá type hints ani docstring.
# Také neřeší situaci, kdy je zadán neplatný směr převodu.
# V takovém případě by funkce nic nevrátila.

def prevod(hodnota: float, smer: str) -> float:
    """
    Převede hodnotu mezi kilometry a mílemi.

    Parametry:
        hodnota (float): Hodnota určená k převodu.
        smer (str): Směr převodu - "km_to_mi" nebo "mi_to_km".

    Návratová hodnota:
        float: Převedená hodnota.
    """
    if smer == "km_to_mi":
        return hodnota * 0.621371
    elif smer == "mi_to_km":
        return hodnota * 1.60934
    else:
        raise ValueError("Neplatný směr převodu. Použij 'km_to_mi' nebo 'mi_to_km'.")


# Funkce 2:
# Co dělá: Přidává souřadnice bodu do seznamu a vypisuje informaci o přidaném bodu a aktuálním počtu bodů.
# Má nějaký problém? Ano. Používá globální proměnnou 'souradnice', což není ideální.
# Funkce je pak závislá na proměnné mimo sebe a hůře se znovu používá.
# Lepší je předat seznam souřadnic jako parametr.

souradnice: list[list[float]] = []


def pridej_bod(souradnice: list[list[float]], lat: float, lon: float) -> None:
    """
    Přidá bod do seznamu souřadnic a vypíše informace.

    Parametry:
        souradnice (list[list[float]]): Seznam souřadnic.
        lat (float): Zeměpisná šířka bodu.
        lon (float): Zeměpisná délka bodu.

    Návratová hodnota:
        None
    """
    souradnice.append([lat, lon])
    print(f"Přidán bod: {lat}, {lon}")
    print(f"Celkem bodů: {len(souradnice)}")
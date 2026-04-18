import json
from pathlib import Path


def vypocitej_vzdalenost_od_rovniku(
    sirka: float, jednotka: str = "km", zaokrouhlit: bool = False
) -> float | int:
    """Vypocte vzdalenost bodu od rovniku.

    Args:
        sirka: Zemepisna sirka ve stupnich.
        jednotka: Pozadovana jednotka vysledku, "km" nebo "mile".
        zaokrouhlit: Pokud je True, vysledek se zaokrouhli na cele cislo.

    Returns:
        Vzdalenost od rovniku v pozadovane jednotce.
    """
    km_na_stupen = 111.32
    vzdalenost_km = abs(sirka) * km_na_stupen

    if jednotka == "km":
        vzdalenost: float | int = vzdalenost_km
    elif jednotka == "mile":
        vzdalenost = vzdalenost_km * 0.621371
    else:
        raise ValueError("Neplatna jednotka. Pouzijte 'km' nebo 'mile'.")

    if zaokrouhlit:
        vzdalenost = round(vzdalenost)

    return vzdalenost


def vytvor_geojson_bod(nazev: str, lat: float, lon: float) -> str:
    """Vytvori GeoJSON bod s nazvem mista a vzdalenosti od rovniku.

    Args:
        nazev: Nazev bodu.
        lat: Zemepisna sirka bodu.
        lon: Zemepisna delka bodu.

    Returns:
        Formatovany GeoJSON retezec s geometrii typu Point.
    """
    vzdalenost_od_rovniku = vypocitej_vzdalenost_od_rovniku(lat)
    geojson_bod = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [lon, lat],
        },
        "properties": {
            "nazev": nazev,
            "vzdalenost_od_rovniku": vzdalenost_od_rovniku,
        },
    }
    return json.dumps(geojson_bod, ensure_ascii=False, indent=2)


# Cast B - analyza a oprava funkce 1:
# Funkce prevadi vzdalenost mezi kilometry a milemi podle zadaneho smeru.
# Problem je, ze pri neznamem smeru tise vrati None, coz se pak hure odhaluje.
def prevod(hodnota: float, smer: str) -> float:
    if smer == "km_to_mi":
        return hodnota * 0.621371
    if smer == "mi_to_km":
        return hodnota * 1.60934
    raise ValueError("Neplatny smer prevodu. Pouzijte 'km_to_mi' nebo 'mi_to_km'.")


# Cast B - analyza a oprava funkce 2:
# Funkce pridava bod do seznamu souradnic a vypisuje jeho novou velikost.
# Problem je zavislost na globalni promenne, ktera zhorsuje znovupouzitelnost.
def pridej_bod(souradnice: list[list[float]], lat: float, lon: float) -> int:
    souradnice.append([lat, lon])
    print(f"Pridan bod: {lat}, {lon}")
    print(f"Celkem bodu: {len(souradnice)}")
    return len(souradnice)


sirky_mest = [0, 15, 30, 45, 60]
vypoctene_vzdalenosti = []
nastaveni_vypoctu = [
    ("km", False),
    ("km", True),
    ("mile", False),
    ("mile", True),
]

for sirka in sirky_mest:
    for jednotka, zaokrouhlit in nastaveni_vypoctu:
        vzdalenost = vypocitej_vzdalenost_od_rovniku(sirka, jednotka, zaokrouhlit)
        vypoctene_vzdalenosti.append((sirka, vzdalenost, jednotka))

for sirka, vzdalenost, jednotka in vypoctene_vzdalenosti:
    print(f"Mesto na sirce {sirka} stupnu je {vzdalenost} {jednotka} od rovniku.")


nazev_mista = "Praha"
lat_mista = 50.0755
lon_mista = 14.4378

geojson_text = vytvor_geojson_bod(nazev_mista, lat_mista, lon_mista)
vystupni_soubor = Path(__file__).with_name("misto_Svoboda.geojson")
vystupni_soubor.write_text(geojson_text, encoding="utf-8")

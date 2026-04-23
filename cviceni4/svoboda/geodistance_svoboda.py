import json
from pathlib import Path


KM_NA_STUPEN = 111.32
KM_NA_MILI = 0.621371


def vypocitej_vzdalenost_od_rovniku(
    sirka: float,
    jednotka: str = "km",
    zaokrouhlit: bool = False,
) -> float:
    """
    Vypocita vzdalenost bodu od rovniku podle zemske sirky.

    Parametry:
        sirka: Zemepisna sirka ve stupnich.
        jednotka: Pozadovana jednotka vysledku, "km", "mi" nebo "mile".
        zaokrouhlit: Pokud je True, vysledek se zaokrouhli na cele cislo.

    Navratova hodnota:
        Vzdalenost od rovniku v pozadovane jednotce.
    """
    vzdalenost_km = abs(sirka) * KM_NA_STUPEN
    normalizovana_jednotka = jednotka.lower()

    if normalizovana_jednotka == "km":
        vysledek = vzdalenost_km
    elif normalizovana_jednotka in {"mi", "mile"}:
        vysledek = vzdalenost_km * KM_NA_MILI
    else:
        raise ValueError("Neplatna jednotka. Pouzij 'km', 'mi' nebo 'mile'.")

    if zaokrouhlit:
        vysledek = round(vysledek)

    return float(vysledek)


def vytvor_geojson_bod(nazev: str, lat: float, lon: float) -> str:
    """
    Vytvori GeoJSON bod s nazvem mista a vzdalenosti od rovniku.

    Parametry:
        nazev: Nazev bodu.
        lat: Zemepisna sirka bodu.
        lon: Zemepisna delka bodu.

    Navratova hodnota:
        Textovy retezec s validnim GeoJSON bodem.
    """
    geojson_bod = {
        "type": "Feature",
        "properties": {
            "nazev": nazev,
            "vzdalenost_od_rovniku": round(
                vypocitej_vzdalenost_od_rovniku(lat),
                2,
            ),
        },
        "geometry": {
            "type": "Point",
            "coordinates": [lon, lat],
        },
    }
    return json.dumps(geojson_bod, ensure_ascii=False, indent=2)


# Funkce prevadi hodnotu mezi kilometry a milemi podle zvoleneho smeru.
# Problem puvodni verze je, ze neresi neplatny smer prevodu, a mohla by tak vratit None.
def prevod(hodnota: float, smer: str) -> float:
    """Prevede hodnotu mezi kilometry a milemi."""
    if smer == "km_to_mi":
        return hodnota * KM_NA_MILI
    if smer == "mi_to_km":
        return hodnota / KM_NA_MILI
    raise ValueError("Neplatny smer prevodu. Pouzij 'km_to_mi' nebo 'mi_to_km'.")


# Funkce pridava bod do seznamu souradnic a vypisuje informace o poctu bodu.
# Problem puvodni verze je pouziti globalni promenne, ktera funkci zbytecne svazuje s okolim.
def pridej_bod(souradnice: list[list[float]], lat: float, lon: float) -> None:
    """Prida bod do predaneho seznamu souradnic a vypise zakladni informaci."""
    souradnice.append([lat, lon])
    print(f"Pridan bod: {lat}, {lon}")
    print(f"Celkem bodu: {len(souradnice)}")


def main() -> None:
    sirky = [0, 15, 30, 45, 60]
    kombinace = [
        ("km", False),
        ("mile", False),
        ("km", True),
        ("mile", True),
    ]

    for sirka in sirky:
        for jednotka, zaokrouhlit in kombinace:
            vzdalenost = vypocitej_vzdalenost_od_rovniku(
                sirka,
                jednotka=jednotka,
                zaokrouhlit=zaokrouhlit,
            )

            if zaokrouhlit:
                print(
                    f"Mesto na sirce {sirka}° je {vzdalenost:.0f} "
                    f"{jednotka} od rovniku."
                )
            else:
                print(
                    f"Mesto na sirce {sirka}° je {vzdalenost:.2f} "
                    f"{jednotka} od rovniku."
                )

    geojson_text = vytvor_geojson_bod("Praha", 50.0755, 14.4378)
    vystupni_soubor = Path(__file__).with_name("misto_svoboda.geojson")
    vystupni_soubor.write_text(geojson_text, encoding="utf-8")
    print(f"\nGeoJSON byl ulozen do souboru {vystupni_soubor.name}.")


if __name__ == "__main__":
    main()

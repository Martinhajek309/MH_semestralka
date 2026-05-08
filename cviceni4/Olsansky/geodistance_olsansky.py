import json
from pathlib import Path


def vypocitej_vzdalenost_od_rovniku(
    sirka: float,
    jednotka: str = "km",
    zaokrouhlit: bool = False,
) -> float | int:
    """Vypočítá vzdálenost od rovníku pro zadanou zeměpisnou šířku.

    Args:
        sirka: Zeměpisná šířka ve stupních.
        jednotka: Jednotka výsledku ("km" nebo "mile"). Výchozí je "km".
        zaokrouhlit: Pokud je True, vrátí zaokrouhlenou hodnotu na celé číslo.

    Returns:
        Vzdálenost od rovníku v zadané jednotce.
    """
    km_na_stupen = 111.32
    km_na_mili = 0.621371

    vzdalenost_km = abs(sirka) * km_na_stupen

    if jednotka == "km":
        vzdalenost = vzdalenost_km
    elif jednotka in ("mile", "miles"):
        vzdalenost = vzdalenost_km * km_na_mili
    else:
        raise ValueError("Neplatná jednotka. Použijte 'km' nebo 'mile'.")

    if zaokrouhlit:
        return round(vzdalenost)

    return vzdalenost


def vytvor_geojson_bod(nazev: str, lat: float, lon: float) -> str:
    """Vytvoří GeoJSON bod s názvem a vzdáleností od rovníku.

    Args:
        nazev: Název bodu.
        lat: Zeměpisná šířka bodu.
        lon: Zeměpisná délka bodu.

    Returns:
        Textový řetězec obsahující validní GeoJSON Feature bod.
    """
    vzdalenost_od_rovniku = vypocitej_vzdalenost_od_rovniku(lat, "km", False)

    geojson = {
        "type": "Feature",
        "properties": {
            "nazev": nazev,
            "vzdalenost_od_rovniku": round(float(vzdalenost_od_rovniku), 2),
        },
        "geometry": {
            "type": "Point",
            "coordinates": [lon, lat],
        },
    }

    return json.dumps(geojson, ensure_ascii=False, indent=2)


lista_sirek = [0, 15, 30, 45, 60, 75, 90]
kombinace_parametru = [
    ("km", False),
    ("km", True),
    ("mile", False),
    ("mile", True),
]

for sirka in lista_sirek:
    for jednotka, zaokrouhlit in kombinace_parametru:
        vzdalenost = vypocitej_vzdalenost_od_rovniku(sirka, jednotka, zaokrouhlit)
        if isinstance(vzdalenost, float):
            vzdalenost = round(vzdalenost, 2)
        print(f"Město na šířce {sirka}° je {vzdalenost} {jednotka} od rovníku.")


geojson_bod = vytvor_geojson_bod("Praha", 50.0755, 14.4378)
vystupni_soubor = Path(__file__).with_name("misto_olsansky.geojson")
vystupni_soubor.write_text(geojson_bod, encoding="utf-8")
print(f"GeoJSON uložen do: {vystupni_soubor}")


#Funkce na převod mezi kilometry a mílemi, je funkční ALE Pokud uživatel zadá jiný směr než
#"km_to_mi" nebo "mi_to_km", funkce nic nevrátí. To může být problém, protože uživatel nepozná

def prevod(hodnota, smer):
    if smer == "km_to_mi":
        return hodnota * 0.621371
    if smer == "mi_to_km":
        return hodnota * 1.60934
    else:
        print("Neplatný směr převodu. Použijte 'km_to_mi' nebo 'mi_to_km'.")
        return None


# Funkce pro přidávání bodů do seznamu, je funkční ALE Poslední print("Celkem bodů...") je mimo funkci,
# takže se nevykoná po přidání bodu, ale jen jednou při spuštění programu.
# Správně má být uvnitř funkce.

souradnice = []

def pridej_bod(lat, lon):
    souradnice.append((lat, lon))
    print(f"Přidán bod: {lat}, {lon}")
    print(f"Celkem bodů: {len(souradnice)}")
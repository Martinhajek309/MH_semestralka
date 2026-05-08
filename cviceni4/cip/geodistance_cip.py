# geodistance_cip.py

def vypocitej_vzdalenost_od_rovniku(sirka: float, jednotka: str = "km", zaokrouhlit: bool = False) -> float:
    """
    Vypočítá vzdálenost od rovníku pro zadanou zeměpisnou šířku.

    Args:
        sirka (float): Zeměpisná šířka ve stupních.
        jednotka (str, optional): Jednotka vzdálenosti ("km" nebo "mi"). Defaults to "km".
        zaokrouhlit (bool, optional): Zda zaokrouhlit výsledek na celé číslo. Defaults to False.

    Returns:
        float: Vzdálenost od rovníku v zadané jednotce.
    """
    vzdalenost_km = abs(sirka) * 111.32
    if jednotka == "mi":
        vzdalenost = vzdalenost_km * 0.621371
    else:
        vzdalenost = vzdalenost_km
    if zaokrouhlit:
        vzdalenost = round(vzdalenost)
    return vzdalenost

def vytvor_geojson_bod(nazev: str, lat: float, lon: float) -> str:
    """
    Vytvoří GeoJSON řetězec pro bod s názvem a vzdáleností od rovníku.

    Args:
        nazev (str): Název bodu.
        lat (float): Zeměpisná šířka.
        lon (float): Zeměpisná délka.

    Returns:
        str: GeoJSON řetězec pro bod.
    """
    vzdalenost = vypocitej_vzdalenost_od_rovniku(lat)
    geojson = f'''{{
  "type": "Feature",
  "geometry": {{
    "type": "Point",
    "coordinates": [{lon}, {lat}]
  }},
  "properties": {{
    "nazev": "{nazev}",
    "vzdalenost_od_rovniku": {vzdalenost}
  }}
}}'''
    return geojson

# Funkce 1: Kontrola a oprava původní funkce prevod
# Co dělá? Převede hodnotu mezi kilometry a mílemi podle směru zadaného jako text.
# Má problém? Původní verze neměla type hints, chyběl jasný else blok pro neplatný směr a
# používala dvě samostatná if podmínky místo if/elif, což může být méně čitelné.

def prevod(hodnota: float, smer: str) -> float:
    """
    Převede hodnotu mezi kilometry a mílemi podle zadaného směru.

    Args:
        hodnota (float): Číselná hodnota k převodu.
        smer (str): Směr převodu, buď "km_to_mi" nebo "mi_to_km".

    Returns:
        float: Převedená hodnota v požadované jednotce.

    Raises:
        ValueError: Pokud je směrový parametr neplatný.
    """
    if smer == "km_to_mi":
        return hodnota * 0.621371
    elif smer == "mi_to_km":
        return hodnota * 1.60934
    else:
        raise ValueError(f"Neplatný směr převodu: {smer}. Použijte 'km_to_mi' nebo 'mi_to_km'.")


# Funkce 2: Kontrola a oprava původní funkce pridej_bod
# Co dělá? Přidává nový bod do seznamu souřadnic a vypisuje informace.
# Má problém? Původní verze používala globální seznam, neposkytovala type hints a nevracela aktualizovaný seznam.

def pridej_bod(lat: float, lon: float, souradnice: list[list[float]]) -> list[list[float]]:
    """
    Přidá bod do seznamu souřadnic.

    Args:
        lat (float): Zeměpisná šířka bodu.
        lon (float): Zeměpisná délka bodu.
        souradnice (list[list[float]]): Seznam souřadnic, do kterého se bod přidá.

    Returns:
        list[list[float]]: Aktualizovaný seznam souřadnic.
    """
    souradnice.append([lat, lon])
    print(f"Přidán bod: {lat}, {lon}")
    print(f"Celkem bodů: {len(souradnice)}")
    return souradnice


# Úkol 1: Základy funkcí
# Poznámka: Funkce je rozšířena pro následující úkoly, ale pro úkol 1 stačí základní volání.

sirky = [0, 15, 30, 45, 60]

for sirka in sirky:
    vzdalenost = vypocitej_vzdalenost_od_rovniku(sirka)
    print(f"Město na šířce {sirka}° je {vzdalenost} km od rovníku.")

# Úkol 2: Parametry, return a type hints
# Rozšířená funkce s parametry

# Příklady volání s různými parametry
for sirka in sirky:
    # V km, nezaokrouhleno
    vzdalenost_km = vypocitej_vzdalenost_od_rovniku(sirka)
    print(f"Město na šířce {sirka}° je {vzdalenost_km} km od rovníku.")
    
    # V mílích, zaokrouhleno
    vzdalenost_mi = vypocitej_vzdalenost_od_rovniku(sirka, jednotka="mi", zaokrouhlit=True)
    print(f"Město na šířce {sirka}° je {vzdalenost_mi} mi od rovníku.")

# Úkol 3: Dokumentace a kvalita kódu
# Docstringy přidány, funkce vytvor_geojson_bod vytvořena

# Volání pro existující místo - Praha
geojson_praha = vytvor_geojson_bod("Praha", 50.0755, 14.4378)

# Uložení do souboru
with open("misto_cip.geojson", "w", encoding="utf-8") as f:
    f.write(geojson_praha)

print("GeoJSON soubor 'misto_cip.geojson' byl vytvořen.")
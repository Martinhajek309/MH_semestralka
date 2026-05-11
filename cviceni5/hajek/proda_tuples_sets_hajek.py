# Úkol 1: Tuples (Blok L7-1)

# 1. Seznam tuples s 10 českými městy
# Struktura každého tuple: (nazev, lat, lon, kategorie)

mesta = [
    ("Praha", 50.0755, 14.4378, "krajské"),
    ("Brno", 49.1951, 16.6068, "krajské"),
    ("Olomouc", 49.5938, 17.2509, "historické"),
    ("Karlovy Vary", 50.2319, 12.8710, "lázeňské"),
    ("Plzeň", 49.7384, 13.3736, "krajské"),
    ("Kutná Hora", 49.9484, 15.2682, "historické"),
    ("Přerov", 49.4551, 17.4509, "okresní"),
    ("Třeboň", 49.0036, 14.7706, "lázeňské"),
    ("Znojmo", 48.8555, 16.0488, "historické"),
    ("Jihlava", 49.3961, 15.5902, "okresní"),
]


# 2. Výpis všech měst pomocí rozbalení tuple
print("Seznam měst:")
for nazev, lat, lon, kategorie in mesta:
    print(f"{nazev}: {lat}°N, {lon}°E ({kategorie})")


# 3. Funkce pro ověření, zda bod leží v zadané oblasti
def je_v_oblasti(souradnice, min_lat, max_lat, min_lon, max_lon):
    """
    Funkce přijme tuple souřadnic (lat, lon)
    a vrátí True, pokud bod leží v zadané oblasti.
    """
    lat, lon = souradnice

    return min_lat <= lat <= max_lat and min_lon <= lon <= max_lon


# 4. Rozdělení měst na západní a východní pomocí list comprehension
# Hranice je zvolena podle zeměpisné délky 15.5°E
hranice_lon = 15.5

zapadni_mesta = tuple([
    mesto for mesto in mesta
    if je_v_oblasti((mesto[1], mesto[2]), 48.0, 51.5, 12.0, hranice_lon)
])

vychodni_mesta = tuple([
    mesto for mesto in mesta
    if je_v_oblasti((mesto[1], mesto[2]), 48.0, 51.5, hranice_lon, 19.0)
])


print("\nZápadní města:")
for nazev, lat, lon, kategorie in zapadni_mesta:
    print(f"{nazev}: {lat}°N, {lon}°E ({kategorie})")


print("\nVýchodní města:")
for nazev, lat, lon, kategorie in vychodni_mesta:
    print(f"{nazev}: {lat}°N, {lon}°E ({kategorie})")

    # Úkol 2: Sets (Blok L7-2)

# 1. Vytvoření setů kategorií z východních a západních měst
kategorie_vychod = {kategorie for nazev, lat, lon, kategorie in vychodni_mesta}
kategorie_zapad = {kategorie for nazev, lat, lon, kategorie in zapadni_mesta}

print("\nKategorie východních měst:")
print(kategorie_vychod)

print("\nKategorie západních měst:")
print(kategorie_zapad)


# 2. Kontrola, zda kategorie východního města existuje také mezi západními kategoriemi
print("\nKontrola kategorií východních měst proti západním kategoriím:")

for nazev, lat, lon, kategorie in vychodni_mesta:
    if kategorie in kategorie_zapad:
        print(f"{nazev}: kategorie '{kategorie}' existuje i mezi západními městy.")
    else:
        print(f"{nazev}: kategorie '{kategorie}' neexistuje mezi západními městy.")


# 3. Pro každou unikátní kategorii ze západního setu vypíšeme všechna města,
# která do ní spadají, a to z východních i západních měst.
print("\nMěsta podle kategorií ze západního setu:")

vsechna_mesta = vychodni_mesta + zapadni_mesta

for kategorie in kategorie_zapad:
    print(f"\nKategorie: {kategorie}")

    for nazev, lat, lon, kat_mesta in vsechna_mesta:
        if kat_mesta == kategorie:
            print(f"- {nazev}")

            # Úkol 3: Množinové operace (Blok L7-3)

# 1. Vytvoření dvou prázdných setů
turisticke_atrakce = set()
prirodni_rezervace = set()


# 2. Funkce pro zařazení města do zadaného setu
def zarad_mesto(mesto, cilovy_set):
    """
    Funkce přijme celý tuple města a vloží ho do zadaného setu.
    """
    cilovy_set.add(mesto)


# Zařazení měst do setů
# Některá města jsou v obou setech, některá pouze v jednom.

for mesto in mesta:
    nazev, lat, lon, kategorie = mesto

    if nazev in ["Praha", "Olomouc", "Kutná Hora", "Karlovy Vary", "Třeboň"]:
        zarad_mesto(mesto, turisticke_atrakce)

    if nazev in ["Karlovy Vary", "Třeboň", "Znojmo", "Jihlava", "Olomouc"]:
        zarad_mesto(mesto, prirodni_rezervace)


# Pomocná funkce pro přehledný výpis měst ze setu
def vypis_mesta(nadpis, mnozina_mest):
    print(f"\n{nadpis}")

    if not mnozina_mest:
        print("Žádná města.")
    else:
        for nazev, lat, lon, kategorie in mnozina_mest:
            print(f"- {nazev}: {lat}°N, {lon}°E ({kategorie})")


# 3. Množinové operace

# Města, která jsou turistickou atrakcí NEBO přírodní rezervací
mesta_unie = turisticke_atrakce | prirodni_rezervace

# Města, která jsou současně turistickou atrakcí I přírodní rezervací
mesta_prunik = turisticke_atrakce & prirodni_rezervace

# Města, která jsou turistickou atrakcí, ale NEJSOU přírodní rezervací
mesta_rozdil = turisticke_atrakce - prirodni_rezervace

# Města, která jsou BUĎ turistickou atrakcí, NEBO přírodní rezervací, ale ne obojím
mesta_symetricky_rozdil = turisticke_atrakce ^ prirodni_rezervace


# Výpis výsledků
vypis_mesta(
    "Města, která jsou turistickou atrakcí NEBO přírodní rezervací:",
    mesta_unie
)

vypis_mesta(
    "Města, která jsou současně turistickou atrakcí I přírodní rezervací:",
    mesta_prunik
)

vypis_mesta(
    "Města, která jsou turistickou atrakcí, ale NEJSOU přírodní rezervací:",
    mesta_rozdil
)

vypis_mesta(
    "Města, která jsou BUĎ turistickou atrakcí, NEBO přírodní rezervací, ale ne obojím:",
    mesta_symetricky_rozdil
)
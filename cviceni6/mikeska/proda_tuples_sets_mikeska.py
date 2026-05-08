"""
Cvičení 6 - Tuples a Sets
"""

# Úkol 1: Tuples

# 1. Vytvořte seznam tuples obsahující 10 českých měst.
mesta = [
    ("Palkovice", 49.6711, 18.3239, "obec"),
    ("Hukvaldy", 49.6219, 18.2247, "turistické"),
    ("Kozlovice", 49.6153, 18.2619, "obec"),
    ("Frýdlant nad Ostravicí", 49.5919, 18.3606, "obec"),
    ("Ostravice", 49.5333, 18.3833, "turistické"),
    ("Čeladná", 49.5500, 18.3333, "turistické"),
    ("Staré Hamry", 49.4833, 18.4500, "obec"),
    ("Morávka", 49.5989, 18.5258, "obec"),
    ("Raškovice", 49.6558, 18.4553, "obec"),
    ("Janovice", 49.6553, 18.3806, "obec"),
]

# 2. Vypište všechna města pomocí rozbalení tuple.
print("--- Seznam měst ---")
for nazev, lat, lon, kategorie in mesta:
    print(f"{nazev}: {lat}°N, {lon}°E ({kategorie})")
print("-" * 20)

# 3. Vytvořte funkci je_v_oblasti.
def je_v_oblasti(souradnice, min_lat, max_lat, min_lon, max_lon):
    """Zjistí, zda se souřadnice nachází v dané oblasti."""
    lat, lon = souradnice
    return min_lat <= lat <= max_lat and min_lon <= lon <= max_lon

# 4. Rozdělte města na východní a západní.
hranice_lon = 15.0
zapadni_mesta = tuple([mesto for mesto in mesta if mesto[2] < hranice_lon])
vychodni_mesta = tuple([mesto for mesto in mesta if mesto[2] >= hranice_lon])

print("\n--- Západní města ---")
for nazev, _, _, _ in zapadni_mesta:
    print(nazev)

print("\n--- Východní města ---")
for nazev, _, _, _ in vychodni_mesta:
    print(nazev)
print("-" * 20)


# Úkol 2: Sets

# 1. Vytvořte sety kategorií.
kategorie_zapad = {mesto[3] for mesto in zapadni_mesta}
kategorie_vychod = {mesto[3] for mesto in vychodni_mesta}

print(f"\nKategorie západních měst: {kategorie_zapad}")
print(f"Kategorie východních měst: {kategorie_vychod}")
print("-" * 20)

# 2. Zjistěte, zda kategorie východních měst existuje v setu západních.
print("\n--- Kontrola kategorií východních měst v západních ---")
for mesto in vychodni_mesta:
    nazev, _, _, kategorie = mesto
    if kategorie in kategorie_zapad:
        print(f"Kategorie '{kategorie}' města {nazev} existuje i na západě.")
    else:
        print(f"Kategorie '{kategorie}' města {nazev} je unikátní pro východ.")
print("-" * 20)

# 3. Vypište města pro každou unikátní kategorii ze západního setu.
print("\n--- Města podle kategorií (ze západního setu) ---")
for kategorie in kategorie_zapad:
    mesta_v_kategorii = [mesto[0] for mesto in mesta if mesto[3] == kategorie]
    print(f"Kategorie '{kategorie}': {', '.join(mesta_v_kategorii)}")
print("-" * 20)


# Úkol 3: Množinové operace

# 1. Vytvořte dva prázdné sety.
turisticke_atrakce = set()
prirodni_rezervace = set()

# 2. Implementujte funkci zarad_mesto a zařaďte města.
def zarad_mesto(mesto, cilovy_set):
    """Vloží město do zadaného setu."""
    cilovy_set.add(mesto)

# Zařazení měst (příklad)
zarad_mesto(mesta[0], turisticke_atrakce) # Praha
zarad_mesto(mesta[3], turisticke_atrakce) # Český Krumlov
zarad_mesto(mesta[4], turisticke_atrakce) # Kutná Hora
zarad_mesto(mesta[8], turisticke_atrakce) # Telč
zarad_mesto(mesta[9], turisticke_atrakce) # Liberec (Ještěd)

zarad_mesto(mesta[2], prirodni_rezervace) # Karlovy Vary (lesy)
zarad_mesto(mesta[7], prirodni_rezervace) # Mariánské Lázně (lesy)
zarad_mesto(mesta[9], prirodni_rezervace) # Liberec (Jizerské hory)
zarad_mesto(mesta[3], prirodni_rezervace) # Český Krumlov (Blanský les)


# 3. Množinové operace
print("\n--- Množinové operace ---")

# Unie (|)
print("\nTuristická atrakce NEBO přírodní rezervace:")
for mesto in turisticke_atrakce | prirodni_rezervace:
    print(f"- {mesto[0]}")

# Průnik (&)
print("\nTuristická atrakce I přírodní rezervace:")
for mesto in turisticke_atrakce & prirodni_rezervace:
    print(f"- {mesto[0]}")

# Rozdíl (-)
print("\nTuristická atrakce, ale NE přírodní rezervace:")
for mesto in turisticke_atrakce - prirodni_rezervace:
    print(f"- {mesto[0]}")

# Symetrický rozdíl (^)
print("\nBUĎ turistická atrakce, NEBO přírodní rezervace (ale ne obojí):")
for mesto in turisticke_atrakce ^ prirodni_rezervace:
    print(f"- {mesto[0]}")

print("-" * 20)

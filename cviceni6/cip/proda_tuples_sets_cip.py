# proda_tuples_sets_cip

# ÚKOL 1: Tuples a list comprehension

mesta = [
    ("Praha", 50.0755, 14.4378, "krajské"),
    ("Brno", 49.1951, 16.6068, "krajské"),
    ("Ostrava", 49.8209, 18.2625, "krajské"),
    ("Olomouc", 49.5938, 17.2509, "okresní"),
    ("České Budějovice", 48.9757, 14.4800, "okresní"),
    ("Karlovy Vary", 50.2312, 12.8710, "lázeňské"),
    ("Mariánské Lázně", 49.9632, 12.7081, "lázeňské"),
    ("Kutná Hora", 49.9481, 15.2685, "historické"),
    ("Telč", 49.1859, 15.4531, "historické"),
    ("Znojmo", 48.8555, 16.0488, "okresní")
]

print("ÚKOL 1: Seznam tuples českých měst")
for nazev, lat, lon, kategorie in mesta:
    print(f"{nazev}: {lat}°N, {lon}°E ({kategorie})")

# Funkce pro kontrolu, zda bod leží v oblasti

def je_v_oblasti(souradnice, min_lat, max_lat, min_lon, max_lon):
    lat, lon = souradnice
    return min_lat <= lat <= max_lat and min_lon <= lon <= max_lon

# Zvolíme hranici pro rozdělení na východní a západní města
hranice_lon = 15.5

vychodni = tuple([mesto for mesto in mesta if mesto[2] > hranice_lon])
zapadni = tuple([mesto for mesto in mesta if mesto[2] <= hranice_lon])

print("\nÚKOL 1: Rozdělení měst na východní a západní")
print(f"Východní města (lon > {hranice_lon}): {vychodni}")
print(f"Západní města (lon <= {hranice_lon}): {zapadni}")

# Ukázka použití funkce je_v_oblasti
print("\nKontrola oblasti pro první východní a první západní město:")
if vychodni:
    print("   ", vychodni[0][0], "v oblasti?", je_v_oblasti((vychodni[0][1], vychodni[0][2]), 49.0, 50.5, 15.5, 19.0))
if zapadni:
    print("   ", zapadni[0][0], "v oblasti?", je_v_oblasti((zapadni[0][1], zapadni[0][2]), 48.5, 51.0, 12.0, 15.5))

# ÚKOL 2: Sets
print("\nÚKOL 2: Sets kategorií")

vychodni_kategorie = {mesto[3] for mesto in vychodni}
zapadni_kategorie = {mesto[3] for mesto in zapadni}

print(f"Kategorie východních měst: {vychodni_kategorie}")
print(f"Kategorie západních měst: {zapadni_kategorie}")

for mesto in vychodni:
    nazev, lat, lon, kategorie = mesto
    exists = kategorie in zapadni_kategorie
    print(f"{nazev} ({kategorie}): kategorie existuje v západních? {exists}")

print("\nUnikátní kategorie ze západních měst a všechna města v nich:")
for kategorie in zapadni_kategorie:
    vysledek = [mesto[0] for mesto in mesta if mesto[3] == kategorie]
    print(f"   {kategorie}: {vysledek}")

# ÚKOL 3: Množinové operace
print("\nÚKOL 3: Množinové operace")

turisticke_atrakce = set()
prirodni_rezervace = set()


def zarad_mesto(mesto, cilovy_set):
    cilovy_set.add(mesto)

# Rozeřazení měst do setů; některá do obou setů, některá jen do jednoho
zarad_mesto(mesta[0], turisticke_atrakce)          # Praha
zarad_mesto(mesta[1], turisticke_atrakce)          # Brno
zarad_mesto(mesta[1], prirodni_rezervace)
zarad_mesto(mesta[2], prirodni_rezervace)          # Ostrava
zarad_mesto(mesta[3], turisticke_atrakce)          # Olomouc
zarad_mesto(mesta[4], prirodni_rezervace)          # České Budějovice
zarad_mesto(mesta[5], turisticke_atrakce)          # Karlovy Vary
zarad_mesto(mesta[6], turisticke_atrakce)          # Mariánské Lázně
zarad_mesto(mesta[7], prirodni_rezervace)          # Kutná Hora
zarad_mesto(mesta[8], turisticke_atrakce)          # Telč
zarad_mesto(mesta[9], prirodni_rezervace)          # Znojmo

print(f"Turistické atrakce: {turisticke_atrakce}")
print(f"Přírodní rezervace: {prirodni_rezervace}")

vsechny = turisticke_atrakce | prirodni_rezervace
spolecne = turisticke_atrakce & prirodni_rezervace
jen_turisticke = turisticke_atrakce - prirodni_rezervace
exkluzivni = turisticke_atrakce ^ prirodni_rezervace

print("\nMěsta turistická atrakcí NEBO přírodní rezervací:")
for mesto in sorted(vsechny):
    print(f"   {mesto[0]} ({mesto[3]})")

print("\nMěsta současně turistickou atrakcí I přírodní rezervací:")
for mesto in sorted(spolecne):
    print(f"   {mesto[0]} ({mesto[3]})")

print("\nMěsta turistické atrakcí, ale NE přírodní rezervací:")
for mesto in sorted(jen_turisticke):
    print(f"   {mesto[0]} ({mesto[3]})")

print("\nMěsta buď turistická atrakce, nebo přírodní rezervace, ale ne obojí:")
for mesto in sorted(exkluzivni):
    print(f"   {mesto[0]} ({mesto[3]})")

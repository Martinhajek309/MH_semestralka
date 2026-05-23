mesta = [
    ("Nový Jičín", 49.5944, 18.0103, "historické"),
    ("Teplice nad Bečvou", 49.5283, 17.7406, "lázeňské"),
    ("Františkovy Lázně", 50.1203, 12.3517, "lázeňské"),
    ("Znojmo", 48.8555, 16.0488, "historické"),
    ("Kroměříž", 49.2978, 17.3931, "historické"),
    ("Uherské Hradiště", 49.0698, 17.4597, "okresní"),
    ("Jindřichův Hradec", 49.1445, 15.0030, "historické"),
    ("Litomyšl", 49.8707, 16.3126, "historické"),
    ("Děčín", 50.7726, 14.2128, "okresní"),
    ("Třebíč", 49.2150, 15.8817, "historické"),
]

for nazev, lat, lon, kategorie in mesta:
    print(f"{nazev}: {lat}°N, {lon}°E ({kategorie})")


def je_v_oblasti(souradnice, min_lat, max_lat, min_lon, max_lon):
    lat, lon = souradnice
    return min_lat <= lat <= max_lat and min_lon <= lon <= max_lon


hranice = 15.0

vychodni = tuple([
    (nazev, lat, lon, kategorie)
    for nazev, lat, lon, kategorie in mesta
    if lon > hranice
])

zapadni = tuple([
    (nazev, lat, lon, kategorie)
    for nazev, lat, lon, kategorie in mesta
    if lon <= hranice
])

print("\nVýchodní města:")
for m in vychodni:
    print(m)

print("\nZápadní města:")
for m in zapadni:
    print(m)

vychodni_kategorie = {kategorie for _, _, _, kategorie in vychodni}
zapadni_kategorie = {kategorie for _, _, _, kategorie in zapadni}

print("\nKategorie východ:", vychodni_kategorie)
print("Kategorie západ:", zapadni_kategorie)


print("\nPorovnání kategorií (východ vs. západ):")
for nazev, lat, lon, kategorie in vychodni:
    if kategorie in zapadni_kategorie:
        print(f"{nazev} -> kategorie '{kategorie}' JE i na západě")
    else:
        print(f"{nazev} -> kategorie '{kategorie}' NENÍ na západě")


print("\nMěsta podle kategorií (ze západního setu):")

for kat in zapadni_kategorie:
    print(f"\nKategorie: {kat}")
    for nazev, lat, lon, kategorie in mesta:
        if kategorie == kat:
            print((nazev, lat, lon, kategorie))

turisticke_atrakce = set()
prirodni_rezervace = set()


def zarad_mesto(mesto, cilovy_set):
    cilovy_set.add(mesto)


for mesto in mesta:
    nazev, lat, lon, kategorie = mesto

    if kategorie == "lázeňské":
        zarad_mesto(mesto, turisticke_atrakce)
        zarad_mesto(mesto, prirodni_rezervace)

    elif kategorie == "historické":
        zarad_mesto(mesto, turisticke_atrakce)

    elif kategorie == "okresní":
        zarad_mesto(mesto, prirodni_rezervace)


print("\n--- Množinové operace ---")

print("\nTuristická atrakce NEBO přírodní rezervace:")
for m in turisticke_atrakce | prirodni_rezervace:
    print(m)

print("\nTuristická atrakce A zároveň přírodní rezervace:")
for m in turisticke_atrakce & prirodni_rezervace:
    print(m)

print("\nTuristická atrakce, ale NE přírodní rezervace:")
for m in turisticke_atrakce - prirodni_rezervace:
    print(m)

print("\nBUĎ turistická atrakce NEBO přírodní rezervace (ale ne obojí):")
for m in turisticke_atrakce ^ prirodni_rezervace:
    print(m)
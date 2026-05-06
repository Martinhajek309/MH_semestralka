ceska_mesta = [
    ("Praha", 50.0875, 14.4214, "krajské"),
    ("Brno", 49.1951, 16.6068, "krajské"),
    ("Ostrava", 49.8209, 18.2625, "krajské"),
    ("Plzeň", 49.7384, 13.3736, "krajské"),
    ("Liberec", 50.7663, 15.0543, "krajské"),
    ("Olomouc", 49.5955, 17.2518, "krajské"),
    ("Ústí nad Labem", 50.6607, 14.0323, "krajské"),
    ("Přerov", 49.4551, 17.4509, "okresní"),
    ("Mariánské Lázně", 49.9646, 12.7012, "lázeňské"),
    ("Rožnov pod Radhoštěm", 49.4585, 18.1430, "historické")
]

for nazev, lat, lon, kategorie in ceska_mesta:
    print(f"{nazev}: {lat}°N, {lon}°E ({kategorie})")


def je_v_oblasti(souradnice, min_lat, max_lat, min_lon, max_lon):
    lat, lon = souradnice
    return min_lat <= lat <= max_lat and min_lon <= lon <= max_lon


hranice = 15.5

zapadni_mesta = tuple(
    mesto
    for mesto in ceska_mesta
    if je_v_oblasti((mesto[1], mesto[2]), 0, 90, 0, hranice)
)

vychodni_mesta = tuple(
    mesto
    for mesto in ceska_mesta
    if je_v_oblasti((mesto[1], mesto[2]), 0, 90, hranice, 180)
)

print("Západní města:", tuple(mesto[0] for mesto in zapadni_mesta))
print("Východní města:", tuple(mesto[0] for mesto in vychodni_mesta))


vychodni_kategorie = {kategorie for _, _, _, kategorie in vychodni_mesta}
zapadni_kategorie = {kategorie for _, _, _, kategorie in zapadni_mesta}

print("Kategorie východních měst:", vychodni_kategorie)
print("Kategorie západních měst:", zapadni_kategorie)


for nazev, lat, lon, kategorie in vychodni_mesta:
    if kategorie in zapadni_kategorie:
        print(f"{nazev} ({kategorie}) má kategorii i v západních městech.")
    else:
        print(f"{nazev} ({kategorie}) nemá kategorii v západních městech.")


for kategorie in zapadni_kategorie:
    mesta_v_kategorii = [
        nazev
        for nazev, lat, lon, kat in ceska_mesta
        if kat == kategorie
    ]
    print(f"{kategorie}: {', '.join(mesta_v_kategorii)}")


turisticke_atrakce = set()
prirodni_rezervace = set()


def zarad_mesto(mesto, cilovy_set):
    cilovy_set.add(mesto)


for mesto in ceska_mesta:
    nazev, lat, lon, kategorie = mesto

    if kategorie in ("krajské", "historické", "lázeňské"):
        zarad_mesto(mesto, turisticke_atrakce)

    if lon > 16:
        zarad_mesto(mesto, prirodni_rezervace)


print("Turistické atrakce:")
for mesto in turisticke_atrakce:
    print(mesto)


print("Přírodní rezervace:")
for mesto in prirodni_rezervace:
    print(mesto)


print("Města, která jsou turistickou atrakcí NEBO přírodní rezervací:")
for mesto in turisticke_atrakce | prirodni_rezervace:
    print(mesto)


print("Města, která jsou současně turistickou atrakcí I přírodní rezervací:")
for mesto in turisticke_atrakce & prirodni_rezervace:
    print(mesto)


print("Města, která jsou turistickou atrakcí, ale NEJSOU přírodní rezervací:")
for mesto in turisticke_atrakce - prirodni_rezervace:
    print(mesto)


print("Města, která jsou BUĎ turistickou atrakcí, NEBO přírodní rezervací, ale ne obojím:")
for mesto in turisticke_atrakce ^ prirodni_rezervace:
    print(mesto)
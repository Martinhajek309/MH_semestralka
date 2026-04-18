mesta = [
    ("Praha", 50.0755, 14.4378, "historicke"),
    ("Brno", 49.1951, 16.6068, "krajske"),
    ("Ostrava", 49.8209, 18.2625, "krajske"),
    ("Plzen", 49.7384, 13.3736, "krajske"),
    ("Karlovy Vary", 50.2319, 12.8710, "lazenske"),
    ("Marianske Lazne", 49.9646, 12.7012, "lazenske"),
    ("Kutna Hora", 49.9487, 15.2681, "historicke"),
    ("Olomouc", 49.5938, 17.2509, "historicke"),
    ("Liberec", 50.7663, 15.0543, "krajske"),
    ("Znojmo", 48.8555, 16.0488, "okresni"),
]


def je_v_oblasti(souradnice, min_lat, max_lat, min_lon, max_lon):
    lat, lon = souradnice
    return min_lat <= lat <= max_lat and min_lon <= lon <= max_lon


def zarad_mesto(mesto, cilovy_set):
    cilovy_set.add(mesto)


def vypis_mesta(nadpis, kolekce_mest):
    print(f"\n{nadpis}")
    for nazev, lat, lon, kategorie in sorted(kolekce_mest, key=lambda mesto: mesto[0]):
        print(f"- {nazev}: {lat}°N, {lon}°E ({kategorie})")


print("Vsechna mesta:")
for nazev, lat, lon, kategorie in mesta:
    print(f"{nazev}: {lat}°N, {lon}°E ({kategorie})")


hranice_delky = 15.5
vychodni_mesta = tuple(
    [
        mesto
        for mesto in mesta
        if je_v_oblasti((mesto[1], mesto[2]), 48.5, 51.1, hranice_delky, 18.9)
    ]
)
zapadni_mesta = tuple(
    [
        mesto
        for mesto in mesta
        if je_v_oblasti((mesto[1], mesto[2]), 48.5, 51.1, 12.0, hranice_delky)
    ]
)

vypis_mesta("Vychodni mesta:", vychodni_mesta)
vypis_mesta("Zapadni mesta:", zapadni_mesta)


vychodni_kategorie = {kategorie for _, _, _, kategorie in vychodni_mesta}
zapadni_kategorie = {kategorie for _, _, _, kategorie in zapadni_mesta}

print("\nKategorie vychodnich mest:", vychodni_kategorie)
print("Kategorie zapadnich mest:", zapadni_kategorie)

print("\nPorovnani kategorii vychodnich mest se zapadnim setem:")
for nazev, lat, lon, kategorie in vychodni_mesta:
    print(f"{nazev}: kategorie '{kategorie}' je v zapadnich kategoriich? {kategorie in zapadni_kategorie}")

vsechna_rozdelena_mesta = vychodni_mesta + zapadni_mesta
print("\nMesta podle kategorii ze zapadniho setu:")
for kategorie in sorted(zapadni_kategorie):
    mesta_v_kategorii = [nazev for nazev, _, _, kat in vsechna_rozdelena_mesta if kat == kategorie]
    print(f"{kategorie}: {', '.join(mesta_v_kategorii)}")


turisticke_atrakce = set()
prirodni_rezervace = set()

for mesto in mesta:
    if mesto[0] in {"Praha", "Plzen", "Karlovy Vary", "Marianske Lazne", "Kutna Hora", "Olomouc"}:
        zarad_mesto(mesto, turisticke_atrakce)
    if mesto[0] in {"Brno", "Ostrava", "Liberec", "Znojmo", "Karlovy Vary", "Marianske Lazne"}:
        zarad_mesto(mesto, prirodni_rezervace)


vypis_mesta("Turisticke atrakce:", turisticke_atrakce)
vypis_mesta("Prirodni rezervace:", prirodni_rezervace)
vypis_mesta("Turisticka atrakce NEBO prirodni rezervace:", turisticke_atrakce | prirodni_rezervace)
vypis_mesta("Turisticka atrakce I prirodni rezervace:", turisticke_atrakce & prirodni_rezervace)
vypis_mesta("Turisticka atrakce, ale NE prirodni rezervace:", turisticke_atrakce - prirodni_rezervace)
vypis_mesta("Bud turisticka atrakce, nebo prirodni rezervace:", turisticke_atrakce ^ prirodni_rezervace)

"""Prakticke cviceni k tematum tuples a sets."""


mesta = [
    ("Praha", 50.0755, 14.4378, "historicke"),
    ("Brno", 49.1951, 16.6068, "krajske"),
    ("Ostrava", 49.8209, 18.2625, "okresni"),
    ("Plzen", 49.7384, 13.3736, "krajske"),
    ("Olomouc", 49.5938, 17.2509, "historicke"),
    ("Karlovy Vary", 50.2319, 12.8712, "lazenske"),
    ("Ceske Budejovice", 48.9747, 14.4747, "krajske"),
    ("Kutna Hora", 49.9492, 15.2682, "historicke"),
    ("Marianske Lazne", 49.9646, 12.7012, "lazenske"),
    ("Jicin", 50.4353, 15.3516, "okresni"),
]


def je_v_oblasti(souradnice, min_lat, max_lat, min_lon, max_lon):
    """Vrati True, pokud bod lezi uvnitr zadane oblasti."""
    lat, lon = souradnice
    return min_lat <= lat <= max_lat and min_lon <= lon <= max_lon


def zarad_mesto(mesto, cilovy_set):
    """Prida tuple mesta do zvolene mnoziny."""
    cilovy_set.add(mesto)


def vypis_mesta(nadpis, kolekce_mest):
    """Prehledne vypise mesta podle nazvu."""
    print(nadpis)
    for nazev, lat, lon, kategorie in sorted(kolekce_mest, key=lambda mesto: mesto[0]):
        print(f"- {nazev}: {lat}\N{DEGREE SIGN}N, {lon}\N{DEGREE SIGN}E ({kategorie})")


print("Ukol 1: Tuples")
for nazev, lat, lon, kategorie in mesta:
    print(f"{nazev}: {lat}\N{DEGREE SIGN}N, {lon}\N{DEGREE SIGN}E ({kategorie})")

hranice_delky = 15.0

zapadni_mesta = tuple(
    [
        mesto
        for mesto in mesta
        if je_v_oblasti((mesto[1], mesto[2]), 48.0, 51.5, 11.0, hranice_delky)
    ]
)

vychodni_mesta = tuple(
    [
        mesto
        for mesto in mesta
        if je_v_oblasti((mesto[1], mesto[2]), 48.0, 51.5, hranice_delky, 19.0)
    ]
)

print("\nZapadni mesta:")
for mesto in zapadni_mesta:
    print(mesto)

print("\nVychodni mesta:")
for mesto in vychodni_mesta:
    print(mesto)

print("\nUkol 2: Sets")
kategorie_vychod = {kategorie for _, _, _, kategorie in vychodni_mesta}
kategorie_zapad = {kategorie for _, _, _, kategorie in zapadni_mesta}

print(f"Kategorie vychodnich mest: {kategorie_vychod}")
print(f"Kategorie zapadnich mest: {kategorie_zapad}")

for nazev, _, _, kategorie in vychodni_mesta:
    print(
        f"Mesto {nazev} ma kategorii '{kategorie}'. "
        f"Je i mezi zapadnimi kategoriemi? {kategorie in kategorie_zapad}"
    )

vsechna_mesta = vychodni_mesta + zapadni_mesta

for kategorie in sorted(kategorie_zapad):
    mesta_v_kategorii = [
        nazev for nazev, _, _, kategorie_mesta in vsechna_mesta if kategorie_mesta == kategorie
    ]
    print(f"Kategorie '{kategorie}' obsahuje mesta: {', '.join(mesta_v_kategorii)}")

print("\nUkol 3: Mnozinove operace")
turisticke_atrakce = set()
prirodni_rezervace = set()

for mesto in mesta:
    nazev = mesto[0]

    if nazev in {"Praha", "Kutna Hora", "Karlovy Vary", "Marianske Lazne", "Olomouc"}:
        zarad_mesto(mesto, turisticke_atrakce)

    if nazev in {"Karlovy Vary", "Marianske Lazne", "Ceske Budejovice", "Jicin", "Olomouc"}:
        zarad_mesto(mesto, prirodni_rezervace)

vypis_mesta("\nTuristicke atrakce NEBO prirodni rezervace:", turisticke_atrakce | prirodni_rezervace)
vypis_mesta("\nTuristicke atrakce I prirodni rezervace:", turisticke_atrakce & prirodni_rezervace)
vypis_mesta(
    "\nTuristicke atrakce, ale NE prirodni rezervace:",
    turisticke_atrakce - prirodni_rezervace,
)
vypis_mesta(
    "\nPouze jedna z mnozin (symetricky rozdil):",
    turisticke_atrakce ^ prirodni_rezervace,
)

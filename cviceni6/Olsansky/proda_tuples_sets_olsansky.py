mesta = [
	("Praha", 50.0755, 14.4378, "krajské"),
	("Brno", 49.1951, 16.6068, "krajské"),
	("Ostrava", 49.8209, 18.2625, "okresní"),
	("Plzeň", 49.7384, 13.3736, "okresní"),
	("Karlovy Vary", 50.2319, 12.8717, "lázeňské"),
	("Mariánské Lázně", 49.9646, 12.7012, "lázeňské"),
	("Kutná Hora", 49.9484, 15.2682, "historické"),
	("Telč", 49.1842, 15.4527, "historické"),
	("Olomouc", 49.5938, 17.2509, "krajské"),
	("České Budějovice", 48.9747, 14.4749, "okresní"),
]

for nazev, lat, lon, kategorie in mesta:
	print(f"{nazev}: {lat}°N, {lon}°E ({kategorie})")


def je_v_oblasti(souradnice, min_lat, max_lat, min_lon, max_lon):
	lat, lon = souradnice
	return min_lat <= lat <= max_lat and min_lon <= lon <= max_lon


hranice_lon = 15.0

zapadni_mesta = tuple(
	[
		mesto
		for mesto in mesta
		if je_v_oblasti((mesto[1], mesto[2]), 48.0, 51.5, 12.0, hranice_lon)
	]
)

vychodni_mesta = tuple(
	[
		mesto
		for mesto in mesta
		if je_v_oblasti((mesto[1], mesto[2]), 48.0, 51.5, hranice_lon, 19.0)
	]
)

print("\nZápadní města:")
for nazev, lat, lon, kategorie in zapadni_mesta:
	print(f"{nazev}: {lat}°N, {lon}°E ({kategorie})")

print("\nVýchodní města:")
for nazev, lat, lon, kategorie in vychodni_mesta:
	print(f"{nazev}: {lat}°N, {lon}°E ({kategorie})")

vychodni_kategorie = {kategorie for _, _, _, kategorie in vychodni_mesta}
zapadni_kategorie = {kategorie for _, _, _, kategorie in zapadni_mesta}

print("\nVýchodní kategorie:", vychodni_kategorie)
print("Západní kategorie:", zapadni_kategorie)

print("\nKontrola východních měst proti západním kategoriím:")
for nazev, _, _, kategorie in vychodni_mesta:
	print(f"{nazev}: '{kategorie}' je v západních kategoriích? {kategorie in zapadni_kategorie}")

print("\nMěsta podle kategorií ze západního setu:")
for kategorie in zapadni_kategorie:
	mesta_v_kategorii = [
		nazev
		for nazev, _, _, kat in (vychodni_mesta + zapadni_mesta)
		if kat == kategorie
	]
	print(f"{kategorie}: {', '.join(mesta_v_kategorii)}")


turisticke_atrakce = set()
prirodni_rezervace = set()


def zarad_mesto(mesto, cilovy_set):
	cilovy_set.add(mesto)


for mesto in mesta:
	nazev, _, _, _ = mesto

	if nazev in {"Praha", "Kutná Hora", "Telč", "Karlovy Vary", "České Budějovice"}:
		zarad_mesto(mesto, turisticke_atrakce)

	if nazev in {"Karlovy Vary", "Mariánské Lázně", "Olomouc", "Ostrava", "České Budějovice"}:
		zarad_mesto(mesto, prirodni_rezervace)


print("\nMěsta: turistická atrakce NEBO přírodní rezervace (|):")
for nazev, _, _, _ in turisticke_atrakce | prirodni_rezervace:
	print(nazev)

print("\nMěsta: turistická atrakce I přírodní rezervace (&):")
for nazev, _, _, _ in turisticke_atrakce & prirodni_rezervace:
	print(nazev)

print("\nMěsta: turistická atrakce, ale NE přírodní rezervace (-):")
for nazev, _, _, _ in turisticke_atrakce - prirodni_rezervace:
	print(nazev)

print("\nMěsta: BUĎ turistická atrakce, NEBO přírodní rezervace (^):")
for nazev, _, _, _ in turisticke_atrakce ^ prirodni_rezervace:
	print(nazev)

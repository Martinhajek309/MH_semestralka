# ukol 1
mesta = [
    ("Praha", 50.07, 14.43, "krajské"),
    ("Brno", 49.19, 16.61, "krajské"),
    ("Karlovy Vary", 50.23, 12.87, "lázeňské"),
    ("Mariánské Lázně", 49.96, 12.70, "lázeňské"),
    ("Český Krumlov", 48.81, 14.31, "historické"),
    ("Kutná Hora", 49.94, 15.26, "historické"),
    ("Benešov", 49.78, 14.68, "okresní"),
    ("Vyškov", 49.27, 17.00, "okresní"),
    ("Olomouc", 49.59, 17.25, "krajské"),
    ("Telč", 49.18, 15.45, "historické")
]

print("ukol 1: SEZNAM MĚST")
for nazev, lat, lon, kategorie in mesta:
    print(f"{nazev}: {lat}°N, {lon}°E ({kategorie})")

def je_v_oblasti(souradnice, min_lat, max_lat, min_lon, max_lon):
    lat, lon = souradnice
    return min_lat <= lat <= max_lat and min_lon <= lon <= max_lon

hranice_lon = 15.0
zapadni_mesta = tuple([m[0] for m in mesta if m[2] < hranice_lon])
vychodni_mesta = tuple([m[0] for m in mesta if m[2] >= hranice_lon])

print(f"\nZápadní města: {zapadni_mesta}")
print(f"Východní města: {vychodni_mesta}")

# ukol 2
zapadni_data = [m for m in mesta if m[2] < hranice_lon]
vychodni_data = [m for m in mesta if m[2] >= hranice_lon]
set_kategorii_zapad = {m[3] for m in zapadni_data}
set_kategorii_vychod = {m[3] for m in vychodni_data}

print("\n ukol 2: KONTROLA KATEGORIÍ")
for nazev, lat, lon, kategorie in vychodni_data:
    shoda = kategorie in set_kategorii_zapad
    print(f"Město: {nazev} | Shoda s kategorií na západě: {shoda}")

print("\n MĚSTA PODLE ZÁPADNÍCH KATEGORIÍ ")
for kat in set_kategorii_zapad:
    patri_do_kategorie = [m[0] for m in mesta if m[3] == kat]
    print(f"{kat}: {', '.join(patri_do_kategorie)}")

# ukol 3
turisticke_atrakce = set()
prirodni_rezervace = set()

def zarad_mesto(mesto, cilovy_set):
    cilovy_set.add(mesto)

zarad_mesto(mesta[0], turisticke_atrakce)
zarad_mesto(mesta[2], turisticke_atrakce)
zarad_mesto(mesta[4], turisticke_atrakce)
zarad_mesto(mesta[5], turisticke_atrakce)
zarad_mesto(mesta[9], turisticke_atrakce)

zarad_mesto(mesta[2], prirodni_rezervace)
zarad_mesto(mesta[4], prirodni_rezervace)
zarad_mesto(mesta[6], prirodni_rezervace)
zarad_mesto(mesta[7], prirodni_rezervace)

sjednoceni = turisticke_atrakce | prirodni_rezervace
prunik = turisticke_atrakce & prirodni_rezervace
rozdil = turisticke_atrakce - prirodni_rezervace
symetricky_rozdil = turisticke_atrakce ^ prirodni_rezervace

print("\n ukol 3: MNOŽINOVÉ OPERACE")
print(f"Atrakce NEBO rezervace: {[m[0] for m in sjednoceni]}")
print(f"Atrakce I rezervace: {[m[0] for m in prunik]}")
print(f"Atrakce, ale NE rezervace: {[m[0] for m in rozdil]}")
print(f"BUĎ atrakce NEBO rezervace (ne obojí): {[m[0] for m in symetricky_rozdil]}")
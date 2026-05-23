
## Úkol 1: Tuples (Blok L7-1)

mesta = [
    ("Karlovy Vary", 50.23, 12.87, "lázeňské"),
    ("Mariánské Lázně", 49.96, 12.70, "lázeňské"),
    ("Ostrava", 49.8209, 18.2625, "krajské"),
    ("Plzeň", 49.7384, 13.3736, "krajské"),
    ("Liberec", 50.7671, 15.0562, "krajské"),
    ("Olomouc", 49.5938, 17.2509, "krajské"),
    ("Kutná Hora", 49.94, 15.26, "historické"),
    ("Telč", 49.18, 15.45, "historické"),
    ("Benešov", 49.78, 14.68, "okresní"),
    ("Tábor", 49.41, 14.65, "okresní")
]

print(mesta)
for nazev, lat, lon, kategorie in mesta:
    print(f"{nazev}: {lat}°N, {lon}°E ({kategorie})")

def je_v_oblasti(souradnice, min_lat, max_lat, min_lon, max_lon):
    lat, lon = souradnice
    return min_lat <= lat <= max_lat and min_lon <= lon <= max_lon

vychodni_mesta = tuple([m for m in mesta if m[2] >= 15.0])
zapadni_mesta = tuple([m for m in mesta if m[2] < 15.0])

print(f"\nPočet východních měst: {len(vychodni_mesta)}")
print(f"Počet západních měst: {len(zapadni_mesta)}")

## Úkol 2: Sets (Blok L7-2)

kategorie_vychod = {m[3] for m in vychodni_mesta}
kategorie_zapad = {m[3] for m in zapadni_mesta}

print("\n--- východ a západ")
for nazev, lat, lon, kategorie in vychodni_mesta:
    existuje = kategorie in kategorie_zapad
    print(f"Město {nazev} ({kategorie}): Má kategorii i na západě? {existuje}")

print("\n--- západ i východ ---")
vsechna_mesta = mesta
for kat in kategorie_zapad:
    patri_sem = [m[0] for m in vsechna_mesta if m[3] == kat]
    print(f"Kategorie '{kat}': {', '.join(patri_sem)}")

## Úkol 3: Množinové operace (Blok L7-3)

turisticke_atrakce = set()
prirodni_rezervace = set()  

# 2. Funkce pro zařazení
def zarad_mesto(mesto, cilovy_set):
    cilovy_set.add(mesto)

zarad_mesto(mesta[0], turisticke_atrakce) 
zarad_mesto(mesta[2], turisticke_atrakce)
zarad_mesto(mesta[3], turisticke_atrakce)
zarad_mesto(mesta[4], turisticke_atrakce) 
zarad_mesto(mesta[6], turisticke_atrakce) 
zarad_mesto(mesta[8], turisticke_atrakce)

zarad_mesto(mesta[1], prirodni_rezervace)
zarad_mesto(mesta[3], prirodni_rezervace)
zarad_mesto(mesta[5], prirodni_rezervace) 
zarad_mesto(mesta[7], prirodni_rezervace)
zarad_mesto(mesta[9], prirodni_rezervace)

print("\n--- Množinové operace ---")

# Sjednocení 
vse = turisticke_atrakce | prirodni_rezervace
print(f"Atrakce nebo rezervace: {[m[0] for m in vse]}")

# Průnik
oboje = turisticke_atrakce & prirodni_rezervace
print(f"Atrakce i rezervace zároveň: {[m[0] for m in oboje]}")

# Rozdíl 
jen_atrakce = turisticke_atrakce - prirodni_rezervace
print(f"Pouze atrakce (ne rezervace): {[m[0] for m in jen_atrakce]}")

# Symetrický rozdíl 
bud_a_nebo = turisticke_atrakce ^ prirodni_rezervace
print(f"Buď atrakce nebo rezervace (exkluzivně): {[m[0] for m in bud_a_nebo]}")


print("HOTOVO")
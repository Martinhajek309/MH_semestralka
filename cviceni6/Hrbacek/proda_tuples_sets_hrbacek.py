# 1. seznam měst (nazev, lat, lon, kategorie)
mesta = [
    ("Praha", 50.0755, 14.4378, "krajské"),
    ("Brno", 49.1951, 16.6068, "krajské"),
    ("Ostrava", 49.8209, 18.2625, "krajské"),
    ("Karviná", 49.8540, 18.5416, "okresní"),
    ("Olomouc", 49.5938, 17.2509, "krajské"),
    ("Klimkovice", 49.7880, 18.1258, "lázeňské"),
    ("Kutná Hora", 49.9483, 15.2681, "historické"),
    ("Uherské Hradiště", 49.0697, 17.4596, "okresní"),
    ("Český Těšín", 49.7461, 18.6261, "historické"),
    ("Zlín", 49.2244, 17.6628, "krajské"),
]

# 2. výpis pomocí rozbalení tuple
print("=== Seznam měst ===")
for nazev, lat, lon, kategorie in mesta:
    print(f"{nazev}: {lat}°N, {lon}°E ({kategorie})")


# 3. funkce pro kontrolu oblasti
def je_v_oblasti(souradnice, min_lat, max_lat, min_lon, max_lon):
    lat, lon = souradnice
    return min_lat <= lat <= max_lat and min_lon <= lon <= max_lon


# 4. rozdělení na východní a západní (hranice např. 15°E)
hranice = 17

vychodni = tuple(
    mesto for mesto in mesta
    if je_v_oblasti((mesto[1], mesto[2]), 48, 51, 17, 20)
)

zapadni = tuple(
    mesto for mesto in mesta
    if not je_v_oblasti((mesto[1], mesto[2]), 48, 51, 17, 20)
)

print("\n=== Východní města ===")
for m in vychodni:
    print(m[0])

print("\n=== Západní města ===")
for m in zapadni:
    print(m[0])


# 1. set kategorií
kat_vychod = {m[3] for m in vychodni}
kat_zapad = {m[3] for m in zapadni}

print("\nKategorie (východ):", kat_vychod)
print("Kategorie (západ):", kat_zapad)

# 2. kontrola výskytu kategorií
print("\n=== Kontrola kategorií ===")
for m in vychodni:
    if m[3] in kat_zapad:
        print(f"{m[0]} má kategorii i na západě")
    else:
        print(f"{m[0]} má unikátní kategorii")


# 3. výpis měst podle kategorií ze západu
print("\n=== Města podle kategorií (ze západu) ===")
for kat in kat_zapad:
    print(f"\nKategorie: {kat}")
    for m in mesta:
        if m[3] == kat:
            print(f" - {m[0]}")


# 1. vytvoření prázdných množin
turisticke_atrakce = set()
prirodni_rezervace = set()


# 2. funkce pro zařazení
def zarad_mesto(mesto, cilovy_set):
    cilovy_set.add(mesto)


# 3. zařazení měst (můžeš upravit podle sebe)
for m in mesta:
    if m[0] in ["Praha", "Kutná Hora", "Klimkovice"]:
        zarad_mesto(m, turisticke_atrakce)

    if m[0] in ["Klimkovice", "Český Těšín", "Olomouc"]:
        zarad_mesto(m, prirodni_rezervace)


print("\n=== Množinové operace ===")

# 4. OR (sjednocení)
print("\nTuristické NEBO přírodní:")
for m in turisticke_atrakce | prirodni_rezervace:
    print(m[0])

# 5. AND (průnik)
print("\nTuristické A přírodní:")
for m in turisticke_atrakce & prirodni_rezervace:
    print(m[0])

# 6. rozdíl
print("\nTuristické, ale NE přírodní:")
for m in turisticke_atrakce - prirodni_rezervace:
    print(m[0])

# 7. XOR (symetrický rozdíl)
print("\nPouze jedno z nich:")
for m in turisticke_atrakce ^ prirodni_rezervace:
    print(m[0])
"""Ukazka prace se seznamy souradnic."""

# Petiuhelnik zapsany jako seznam bodu [lon, lat].
# Posledni bod opakuje prvni vrchol, aby byl polygon uzavreny.
petiuhelnik = [
    [17.20, 49.60],
    [17.28, 49.64],
    [17.35, 49.60],
    [17.32, 49.53],
    [17.23, 49.52],
    [17.20, 49.60],
]

# Druhy polygon je ctverec, opet uzavreny opakovanim prvniho bodu.
ctverec = [
    [17.40, 49.50],
    [17.48, 49.50],
    [17.48, 49.58],
    [17.40, 49.58],
    [17.40, 49.50],
]

# Multi-polygon obsahuje oba polygony.
multi_polygon = [petiuhelnik, ctverec]

# Indexovanim ziskame druhy vrchol prvniho polygonu.
druhy_vrchol_prvniho_polygonu = multi_polygon[0][1]

# Slicingem ziskame posledni tri vrcholy druheho polygonu v opacnem poradi.
posledni_tri_vrcholy_pozpatku = multi_polygon[1][-1:-4:-1]

print("Petiuhelnik:", petiuhelnik)
print("Ctverec:", ctverec)
print("Multi-polygon:", multi_polygon)
print("Druhy vrchol prvniho polygonu:", druhy_vrchol_prvniho_polygonu)
print("Posledni tri vrcholy druheho polygonu pozpatku:", posledni_tri_vrcholy_pozpatku)

# Trasa je seznam bodu [lon, lat].
trasa = [
    [17.24, 49.58],
    [17.27, 49.60],
    [17.31, 49.61],
    [17.34, 49.59],
]

# Pomoci append pridame novy bod na konec trasy.
trasa.append([17.38, 49.57])

# Pomoci insert vlozime bod doprostred trasy.
trasa.insert(len(trasa) // 2, [17.29, 49.62])

# Funkce sorted vytvori novy seznam bodu serazeny podle lat.
trasa_podle_lat = sorted(trasa, key=lambda bod: bod[1])

# Prumernou souradnici vypocitame zvlast pro lon a lat.
prumerna_lon = sum(bod[0] for bod in trasa) / len(trasa)
prumerna_lat = sum(bod[1] for bod in trasa) / len(trasa)

print("Trasa po pridani bodu:", trasa)
print("Trasa serazena podle lat:", trasa_podle_lat)
print("Prumerna lon souradnice:", prumerna_lon)
print("Prumerna lat souradnice:", prumerna_lat)

# Vyskove body trasy zapiseme jako [lon, lat, vyska].
vyskovy_profil = [
    [17.24, 49.58, 245],
    [17.27, 49.60, 252],
    [17.29, 49.62, 261],
    [17.31, 49.61, 258],
    [17.34, 49.59, 249],
]

# Pomoci enumerate vypiseme poradi bodu a jeho vysku.
for cislo, bod in enumerate(vyskovy_profil, start=1):
    print(f"Bod {cislo}: vyska {bod[2]} m n. m.")

# Spocitame prumernou nadmorskou vysku.
prumerna_vyska = sum(bod[2] for bod in vyskovy_profil) / len(vyskovy_profil)

# List comprehension vytvori body s vyskou vyssi nez prumer.
body_nad_prumerem = [bod for bod in vyskovy_profil if bod[2] > prumerna_vyska]

# Druha list comprehension vytvori seznam obsahujici pouze vysky.
vysky = [bod[2] for bod in vyskovy_profil]

print("Vyskovy profil trasy:", vyskovy_profil)
print("Prumerna nadmorska vyska:", prumerna_vyska)
print("Body s vyskou vyssi nez prumer:", body_nad_prumerem)
print("Pouze vysky z profilu:", vysky)

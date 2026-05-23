# 1) Polygon - petiuhelnik: 5 vrcholu + opakovany prvni bod pro uzavreni
petiuhelnik = [
	[14.4208, 50.0880],
	[14.4220, 50.0892],
	[14.4235, 50.0886],
	[14.4230, 50.0873],
	[14.4212, 50.0870],
	[14.4208, 50.0880],
]

# Druhy polygon (ctverec): 4 vrcholy + opakovany prvni bod pro uzavreni
ctverec = [
	[14.4300, 50.0900],
	[14.4315, 50.0900],
	[14.4315, 50.0885],
	[14.4300, 50.0885],
	[14.4300, 50.0900],
]

# 2) Multi-polygon: seznam polygonu
multi_polygon = [petiuhelnik, ctverec]

# 3) Indexovani: druhy vrchol prvniho polygonu
druhy_vrchol_prvniho_polygonu = multi_polygon[0][1]

# 4) Slicing: posledni tri vrcholy druheho polygonu pozpatku
posledni_tri_vrcholy_druheho_pozpatku = multi_polygon[1][-3:][::-1]

# 5) Vypis vsech vysledku
print("Petiuhelnik:", petiuhelnik)
print("Ctverec:", ctverec)
print("Multi-polygon:", multi_polygon)
print("Druhy vrchol prvniho polygonu:", druhy_vrchol_prvniho_polygonu)
print(
	"Posledni tri vrcholy druheho polygonu (pozpatku):",
	posledni_tri_vrcholy_druheho_pozpatku,
)

# Pokracovani: prace se seznamem bodu trasy

# 1) Trasa: alespon 4 body [lon, lat]
trasa = [
	[14.4100, 50.0800],
	[14.4140, 50.0820],
	[14.4185, 50.0845],
	[14.4220, 50.0860],
]

# 2) Pridani noveho bodu na konec trasy pomoci append
trasa.append([14.4250, 50.0875])

# 3) Vlozeni bodu doprostred trasy pomoci insert
stred_index = len(trasa) // 2
trasa.insert(stred_index, [14.4160, 50.0830])

# 4) Novy seznam bodu serazeny podle lat (y-souradnice)
trasa_serazena_podle_lat = sorted(trasa, key=lambda bod: bod[1])

# 5) Prumerna lon a lat vsech bodu v trase
prumer_lon = sum(bod[0] for bod in trasa) / len(trasa)
prumer_lat = sum(bod[1] for bod in trasa) / len(trasa)

print("Trasa:", trasa)
print("Trasa s novym bodem na konci (append):", trasa)
print("Trasa po vlozeni bodu doprostred (insert):", trasa)
print("Trasa serazena podle lat:", trasa_serazena_podle_lat)
print("Prumerna souradnice [lon, lat]:", [prumer_lon, prumer_lat])


# Pokracovani: prace se seznamem bodu trasy s vyskou


# 1) Seznam bodu [lon, lat, vyska] - vyskovy profil trasy (alespon 5 bodu)
trasa_vyska = [
    [14.4100, 50.0800, 265],
    [14.4125, 50.0815, 272],
    [14.4150, 50.0830, 281],
    [14.4170, 50.0840, 276],
    [14.4200, 50.0860, 289],
]

# 2) Pruchod body pomoci enumerate a formatovany vypis
for cislo, bod in enumerate(trasa_vyska, start=1):
    print(f"Bod {cislo}: vyska {bod[2]} m n. m.")

# 3) Prumerna nadmorska vyska trasy
prumerna_vyska = sum(bod[2] for bod in trasa_vyska) / len(trasa_vyska)

# 4a) Body s vyskou vetsi nez prumer (list comprehension)
body_nad_prumer = [bod for bod in trasa_vyska if bod[2] > prumerna_vyska]

# 4b) Seznam pouze vysek (bez souradnic)
jen_vysky = [bod[2] for bod in trasa_vyska]

# 5) Vypis vysledku s komentari
print("\nVyskovy profil trasy:", trasa_vyska)
print("Prumerna nadmorska vyska:", prumerna_vyska)
print("Body s vyskou vetsi nez prumer:", body_nad_prumer)
print("Pouze vysky:", jen_vysky)


#polygony
pentagon = [[14.4, 50.1], [14.5, 50.1], [14.6, 50.2], [14.5, 50.3], [14.3, 50.2], [14.4, 50.1]]
ctverec = [[16.0, 49.0], [16.1, 49.0], [16.1, 49.1], [16.0, 49.1], [16.0, 49.0]]

#multipolygon
multi_polygon = [pentagon, ctverec]

#vypsání druhého vrcholu prvního polygonu
druhy_vrchol = multi_polygon[0][1]
print(f"druhý vrchol: {druhy_vrchol}") 

#vypsání pozpátku posledních 3 vrcholů druhého polygonu 
reverse = multi_polygon[1][-3:][::-1]
print(f"pozpátku: {reverse}")

#body trasy
trasa = [[14.42, 50.08], [14.44, 50.10], [14.46, 50.12], [14.48, 50.14]]

#připojení bodu do trasy
trasa.append([14.50, 50.16])

#připojení bodu do prostřed - 2 index 
trasa.insert(2, [14.45, 50.11])

#seřazení trasy podle Y
trasa_serazena = sorted(trasa, key=lambda bod: bod[1])

#vypocet
pocet_bodu = len(trasa)
prumerna_lon = sum(bod[0] for bod in trasa) / pocet_bodu
prumerna_lat = sum(bod[1] for bod in trasa) / pocet_bodu

print(f"Průměrná souřadnice trasy: Lon {prumerna_lon:.4f}, Lat {prumerna_lat:.4f}")

#seznam bodů
profil = [
    [14.42, 50.08, 210],
    [14.44, 50.10, 235],
    [14.45, 50.11, 280],
    [14.46, 50.12, 310],
    [14.50, 50.16, 260]
]

for i, bod in enumerate(profil, start=1):
    vyska = bod[2]
    print(f"Bod {i}: výška {vyska} m n. m.")

vysky_list = [bod[2] for bod in profil] 
prumerna_vyska = sum(vysky_list) / len(vysky_list)
print(f"\nPrůměrná výška trasy: {prumerna_vyska} m n. m.")


nadprumerne_body = [bod for bod in profil if bod[2] > prumerna_vyska]

jen_vysky = [bod[2] for bod in profil]

print(f"nadprůměrná výška: {nadprumerne_body}")
print(f"seznam výšek: {jen_vysky}")







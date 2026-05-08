polygon = [[10.0, 0.0], [15.0, 5.0], [10.0, 10.0], [0.0, 10.0], [0.0, 0.0], [10.0, 0.0]]

multipolygon = [
    [[10.0, 0.0], [15.0, 5.0], [10.0, 10.0], [0.0, 10.0], [0.0, 0.0], [10.0, 0.0]],
    [[10.0, 10.0], [0.0, 10.0], [0.0, 0.0], [10.0, 0.0]]
]

druhy_vrchol_polygon = multipolygon[0][1]
posledni_tri_vrcholy = multipolygon[1][-3:][::-1]

print("Druhý vrchol prvního polygonu je:", druhy_vrchol_polygon)
print("Poslední tři vrcholy druhého polygonu v obráceném pořadí jsou:", posledni_tri_vrcholy)

seznam_souradnic = [
    [16.6088, 49.1951],
    [16.6089, 49.1952],
    [16.6090, 49.1953],
    [16.6091, 49.1954]
]

seznam_souradnic.append([16.6092, 49.1955])

seznam_souradnic.insert(2, [16.60895, 49.19525])

serazene_podle_lat = sorted(seznam_souradnic, key=lambda x: x[1])

prumer_lon = sum(bod[0] for bod in seznam_souradnic) / len(seznam_souradnic)
prumer_lat = sum(bod[1] for bod in seznam_souradnic) / len(seznam_souradnic)

print("Původní seznam bodů:", seznam_souradnic)
print("Body seřazené podle lat:", serazene_podle_lat)
print("Průměrná lon souřadnice:", prumer_lon)
print("Průměrná lat souřadnice:", prumer_lat)  

souradnice = [
    [17.2500, 49.5900, 210],
    [17.2510, 49.5910, 215],
    [17.2520, 49.5920, 222],
    [17.2530, 49.5930, 218],
    [17.2540, 49.5940, 225]
]

for i, bod in enumerate(souradnice, start=1):
    print(f"Bod {i}: výška {bod[2]} m n. m.")

prumerna_vyska = sum(bod[2] for bod in souradnice) / len(souradnice)
print("Průměrná výška všech bodů je:", prumerna_vyska, "m n. m.")

body_vyssi_nez_prumer = [bod for bod in souradnice if bod[2] > prumerna_vyska]
vysky = [bod[2] for bod in souradnice]

print("Body s výškou větší než průměr:")
print(body_vyssi_nez_prumer)

print("Seznam všech výšek:")
print(vysky)



petiuhelnik = [
    [15.00, 49.00],
    [15.05, 49.05],
    [15.10, 49.00],
    [15.05, 48.95],
    [15.00, 48.95],
    [15.00, 49.00]
]

ctverec = [
    [15.15, 49.00],
    [15.20, 49.00],
    [15.20, 48.95],
    [15.15, 48.95],
    [15.15, 49.00]
]

multi_polygon = [petiuhelnik, ctverec]

print("Pětiúhelník:", petiuhelnik)
print("Čtverec:", ctverec)
print("Multi-polygon:", multi_polygon)

second_vertex = multi_polygon[0][1]
print("\nDruhý vrchol prvního polygonu:", second_vertex)

last_three_reversed = multi_polygon[1][-3:][::-1]
print("Poslední tři vrcholy druhého polygonu (pozpátku):", last_three_reversed)

trasa = [
    [15.00, 49.00],
    [15.05, 49.05],
    [15.10, 49.00],
    [15.15, 48.95]
]

trasa.append([15.20, 49.00])

trasa.insert(len(trasa)//2, [15.08, 49.02])

serazene = sorted(trasa, key=lambda bod: bod[1])

prumer_lon = sum(bod[0] for bod in trasa) / len(trasa)
prumer_lat = sum(bod[1] for bod in trasa) / len(trasa)

print(trasa)
print(serazene)
print([prumer_lon, prumer_lat])

trasa = [
    [15.00, 49.00, 150],
    [15.05, 49.02, 160],
    [15.10, 49.03, 170],
    [15.15, 49.01, 180],
    [15.20, 49.00, 190]
]

for i, bod in enumerate(trasa, start=1):
    print(f"Bod {i}: výška {bod[2]} m n. m.")

prumer_vyska = sum(bod[2] for bod in trasa) / len(trasa)

vyssi_nez_prumer = [bod for bod in trasa if bod[2] > prumer_vyska]

pouze_vysky = [bod[2] for bod in trasa]

print("\nPrůměrná výška:", prumer_vyska)
print("Body s výškou větší než průměr:", vyssi_nez_prumer)
print("Pouze výšky:", pouze_vysky)

#výsledek: Bod 1: výška 150 m n. m.
#Bod 2: výška 160 m n. m.
#Bod 3: výška 170 m n. m.
#Bod 4: výška 180 m n. m.
#Bod 5: výška 190 m n. m.

#Průměrná výška: 170.0
#Body s výškou větší než průměr: [[15.15, 49.01, 180], [15.2, 49.0, 190]]
#Pouze výšky: [150, 160, 170, 180, 190]
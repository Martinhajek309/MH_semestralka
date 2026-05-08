# polygon = [[15.4, 40.2], [20.1, 30.5], [10.0, 25.3], [5.5, 15.8], ]

# pentagon = [[15.4, 40.2], [20.1, 30.5], [10.0, 25.3], [5.5, 15.8], [8.2, 35.1], [15.4, 40.2]]


# square = [[15.4, 40.2], [20.1, 30.5], [10.0, 25.3], [5.5, 15.8], [15.4, 40.2]]

# multipolygon = polygon + pentagon + square

# print("Polygon:", polygon
#       , "\nPentagon:", pentagon
#       , "\nSquare:", square
#       , "\nMulti-polygon:", multipolygon
#       )

# print("Polygon:", polygon[1]
#       , "\nPentagon:", pentagon[1]
#       , "\nSquare:", square[1]
#       , "\nMulti-polygon:", multipolygon[1])

# print("Polygon[0]:", polygon[0])
# print("Pentagon[0]:", pentagon[0])
# print("Square[0]:", square[0])
# print("Multipolygon[0]:", multipolygon[0])

# print("\nPolygon[2]:", polygon[2])
# print("Pentagon[3]:", pentagon[3])
# print("Square[2]:", square[2])
# print("Multipolygon[5]:", multipolygon[5])


# trasa_ova_celadna = [
#     {"mesto": "Ostrava", "lon": 15.4, "lat": 40.2},
#     {"mesto": "Vratimov", "lon": 20.1, "lat": 30.5},
#     {"mesto": "Paskov", "lon": 10.0, "lat": 25.3},
#     {"mesto": "Liskovec", "lon": 5.5, "lat": 15.8},
#     {"mesto": "Frýdek-Místek", "lon": 8.2, "lat": 35.1},
#     {"mesto": "Čeladna", "lon": 15.4, "lat": 40.2}
# ]

# print("\nTrasa OVA-Celadna (před úpravami):", trasa_ova_celadna)
# trasa_ova_celadna.append({"mesto": "Mesto G", "lon": 12.3, "lat": 22.4})

# trasa_ova_celadna.insert(2, {"mesto": "Mesto H", "lon": 18.5, "lat": 28.7})

# print("\nTrasa OVA-Celadna:", trasa_ova_celadna)

# sorted_by_lat = sorted(trasa_ova_celadna, key=lambda point: point["lat"])
# print("Body seřazené podle lat:", sorted_by_lat)

# avg_lon = sum(point["lon"] for point in trasa_ova_celadna) / len(trasa_ova_celadna)
# avg_lat = sum(point["lat"] for point in trasa_ova_celadna) / len(trasa_ova_celadna)
# print(f"Průměrná souřadnice - lon: {avg_lon:.2f}, lat: {avg_lat:.2f}")
# sorted_by_lat = sorted(trasa_ova_celadna, key=lambda point: point["lat"])
# print("Body seřazené podle lat:", sorted_by_lat)

# Seznam souřadnic [lon, lat, výška]
vystkovy_profil = [
    [15.4, 40.2, 250],
    [20.1, 30.5, 420],
    [10.0, 25.3, 580],
    [5.5, 15.8, 310],
    [8.2, 35.1, 490],
    [15.4, 40.2, 250]
]

# Projekce bodů s čísly
print("Výškový profil trasy:")
for cislo, bod in enumerate(vystkovy_profil, 1):
    print(f"Bod {cislo}: výška {bod[2]} m n. m.")

# Průměrná nadmořská výška
prum_vyska = sum(bod[2] for bod in vystkovy_profil) / len(vystkovy_profil)
print(f"\nPrůměrná nadmořská výška: {prum_vyska:.2f} m n. m.")

# Body s výškou větší než průměr
vysoke_body = [bod for bod in vystkovy_profil if bod[2] > prum_vyska]
print(f"\nBody s výškou větší než průměr: {vysoke_body}")

# Pouze výšky
pouze_vysky = [bod[2] for bod in vystkovy_profil]
print(f"Pouze výšky: {pouze_vysky}")
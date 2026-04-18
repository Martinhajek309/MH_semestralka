# 1. Pětiúhelník (5 vrcholů + uzavření)
polygon1 = [
    [17.25, 49.60],
    [17.30, 49.62],
    [17.35, 49.60],
    [17.33, 49.57],
    [17.27, 49.57],
    [17.25, 49.60]  # uzavření polygonu
]

# 2. Druhý polygon (čtverec)
polygon2 = [
    [17.40, 49.60],
    [17.45, 49.60],
    [17.45, 49.65],
    [17.40, 49.65],
    [17.40, 49.60]  # uzavření
]

# Multi-polygon
multi_polygon = [polygon1, polygon2]

# 3. Druhý vrchol prvního polygonu
second_vertex = multi_polygon[0][1]
print("Druhý vrchol prvního polygonu:", second_vertex)

# 4. Poslední tři vrcholy druhého polygonu pozpátku
last_three_reversed = multi_polygon[1][-3:][::-1]
print("Poslední tři vrcholy druhého polygonu pozpátku:", last_three_reversed)




# 1. Trasa (alespoň 4 body)
route = [
    [17.25, 49.60],
    [17.28, 49.61],
    [17.30, 49.63],
    [17.33, 49.64]
]

# 2. Přidání bodu na konec
route.append([17.35, 49.65])
print("Trasa po append:", route)

# 3. Vložení bodu doprostřed
route.insert(len(route)//2, [17.29, 49.62])
print("Trasa po insert:", route)

# 4. Seřazení podle lat (y)
sorted_route = sorted(route, key=lambda point: point[1])
print("Seřazená trasa podle lat:", sorted_route)

# 5. Průměrná souřadnice
avg_lon = sum(point[0] for point in route) / len(route)
avg_lat = sum(point[1] for point in route) / len(route)

print("Průměrná lon:", avg_lon)
print("Průměrná lat:", avg_lat)



# 1. Výškový profil (lon, lat, výška)
profile = [
    [17.25, 49.60, 210],
    [17.28, 49.61, 220],
    [17.30, 49.63, 250],
    [17.33, 49.64, 240],
    [17.35, 49.65, 230]
]

# 2. Enumerate výpis
for i, point in enumerate(profile):
    print(f"Bod {i}: výška {point[2]} m n. m.")

# 3. Průměrná výška
avg_height = sum(point[2] for point in profile) / len(profile)
print("Průměrná výška:", avg_height)

# 4. List comprehension

# Body s výškou větší než průměr
higher_points = [point for point in profile if point[2] > avg_height]
print("Body nad průměrnou výškou:", higher_points)

# Pouze výšky
heights = [point[2] for point in profile]
print("Seznam výšek:", heights)
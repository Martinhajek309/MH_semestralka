# ukol 1
pentagon = [[0, 0], [2, 0], [3, 2], [1.5, 4], [-1, 2], [0, 0]]
square = [[10, 10], [12, 10], [12, 12], [10, 12], [10, 10]]
multi_polygon = [pentagon, square]
second_vertex_first_poly = multi_polygon[0][1]
last_three_reversed = multi_polygon[1][-3:][::-1]

print(pentagon)
print(multi_polygon)
print(second_vertex_first_poly)
print(last_three_reversed)

# ukol 2
route = [[14.4, 50.1], [14.5, 50.2], [14.6, 50.0], [14.7, 50.3]]
route.append([14.8, 50.4])
middle_index = len(route) // 2
route.insert(middle_index, [14.55, 50.15])
sorted_route = sorted(route, key=lambda p: p[1])
avg_lon = sum(p[0] for p in route) / len(route)
avg_lat = sum(p[1] for p in route) / len(route)

print(route)
print(sorted_route)
print(avg_lon, avg_lat)

# ukol 3 
# 1. Vytvoření seznamu bodů [lon, lat, výška]
elevation_profile = [
    [14.42, 50.08, 230],
    [14.45, 50.10, 255],
    [14.48, 50.12, 310],
    [14.51, 50.15, 290],
    [14.54, 50.18, 340]
]

# 2. Procházení pomocí enumerate a výpis výšek
print("\n--- Výškový profil trasy ---")
for i, point in enumerate(elevation_profile, 1):
    print(f"Bod {i}: výška {point[2]} m n. m.")

# 3. Výpočet průměrné nadmořské výšky
avg_height = sum(point[2] for point in elevation_profile) / len(elevation_profile)
print(f"\nPrůměrná výška: {avg_height} m n. m.")

# 4. List comprehension
# Body s výškou větší než průměr
above_avg = [p for p in elevation_profile if p[2] > avg_height]

# Seznam obsahující pouze výšky
only_heights = [p[2] for p in elevation_profile]

# 5. Výpis výsledků
print("\n--- Analýza výšek ---")
# Výpis bodů nad průměrnou hladinou trasy
print(f"Body s nadprůměrnou výškou: {above_avg}")
# Výpis samostatných hodnot výšek 
print(f"Seznam všech výšek: {only_heights}")
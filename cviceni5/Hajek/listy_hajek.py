pentagon = [
    [14.40, 50.08],
    [14.42, 50.10],
    [14.45, 50.09],
    [14.44, 50.06],
    [14.41, 50.05],
    [14.40, 50.08]
]
square = [
    [15.00, 50.00],
    [15.02, 50.00],
    [15.02, 50.02],
    [15.00, 50.02],
    [15.00, 50.00]
]
multi_polygon =[pentagon,square]
second_vertex_first_polygon = multi_polygon[0][1]
last_three_reversed_second_polygon = multi_polygon[1][-3:][::-1]

print("Pětiúhelník:")
print(pentagon)

print("\nČtverec:")
print(square)

print("\nMulti-polygon:")
print(multi_polygon)

print("\nDruhý vrchol prvního polygonu:")
print(second_vertex_first_polygon)

print("\nPoslední tři vrcholy druhého polygonu seřazené pozpátku:")
print(last_three_reversed_second_polygon)

trasa = [
    [14.40, 50.08],
    [14.42, 50.09],
    [14.44, 50.11],
    [14.46, 50.10]
]
trasa.append([14.48, 50.12])

trasa.insert(2, [14.43, 50.085])

sorted_by_lat = sorted(trasa, key=lambda point: point[1])

average_lon = sum(point[0] for point in trasa) / len(trasa)
average_lat = sum(point[1] for point in trasa) / len(trasa)

print(trasa)
print(sorted_by_lat)
print(average_lon,average_lat)

elevation_profile = [
    [14.40, 50.08, 320],
    [14.42, 50.09, 335],
    [14.44, 50.10, 310],
    [14.46, 50.11, 360],
    [14.48, 50.12, 345]
]
print(elevation_profile)

print("point")
print("\nVýpis jednotlivých bodů a jejich výšek:")
for i, point in enumerate(elevation_profile, start=1):
    print(f"Bod {i}: výška {point[2]} m n. m.")

    average_elevation = sum(point[2] for point in elevation_profile) / len(elevation_profile)

print("\nPrůměrná nadmořská výška trasy:")
print(average_elevation, "m n. m.")

higher_than_average = [point for point in elevation_profile if point[2] > average_elevation]

only_elevations = [point[2] for point in elevation_profile]

print("\nBody s výškou větší než průměr:")
print(higher_than_average)

print("\nSeznam pouze výšek:")
print(only_elevations)

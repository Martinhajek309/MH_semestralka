polygon = [[15.4, 40.2], [20.1, 30.5], [10.0, 25.3], [5.5, 15.8], ]

pentagon = [[15.4, 40.2], [20.1, 30.5], [10.0, 25.3], [5.5, 15.8], [8.2, 35.1], [15.4, 40.2]]


square = [[15.4, 40.2], [20.1, 30.5], [10.0, 25.3], [5.5, 15.8], [15.4, 40.2]]

multipolygon = polygon + pentagon + square

print("Polygon:", polygon
      , "\nPentagon:", pentagon
      , "\nSquare:", square
      , "\nMulti-polygon:", multipolygon
      )

print("Polygon:", polygon[1]
      , "\nPentagon:", pentagon[1]
      , "\nSquare:", square[1]
      , "\nMulti-polygon:", multipolygon[1])

print("Polygon[0]:", polygon[0])
print("Pentagon[0]:", pentagon[0])
print("Square[0]:", square[0])
print("Multipolygon[0]:", multipolygon[0])

print("\nPolygon[2]:", polygon[2])
print("Pentagon[3]:", pentagon[3])
print("Square[2]:", square[2])
print("Multipolygon[5]:", multipolygon[5])


trasa_ova_fm = [
    {"mesto": "Mesto A", "lon": 15.4, "lat": 40.2},
    {"mesto": "Mesto B", "lon": 20.1, "lat": 30.5},
    {"mesto": "Mesto C", "lon": 10.0, "lat": 25.3},
    {"mesto": "Mesto D", "lon": 5.5, "lat": 15.8},
    {"mesto": "Mesto E", "lon": 8.2, "lat": 35.1},
    {"mesto": "Mesto F", "lon": 15.4, "lat": 40.2}
]

trasa_ova_fm.append({"mesto": "Mesto G", "lon": 12.3, "lat": 22.4})

trasa_ova_fm.insert(2, {"mesto": "Mesto H", "lon": 18.5, "lat": 28.7})

print("\nTrasa OVA-FM:", trasa_ova_fm)

sorted_by_lat = sorted(trasa_ova_fm, key=lambda point: point["lat"])
print("Body seřazené podle lat:", sorted_by_lat)

avg_lon = sum(point["lon"] for point in trasa_ova_fm) / len(trasa_ova_fm)
avg_lat = sum(point["lat"] for point in trasa_ova_fm) / len(trasa_ova_fm)
print(f"Průměrná souřadnice - lon: {avg_lon:.2f}, lat: {avg_lat:.2f}")

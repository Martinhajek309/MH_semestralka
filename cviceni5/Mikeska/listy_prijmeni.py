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

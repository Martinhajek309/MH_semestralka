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


polygon = [[15.4, 40.2], [20.1, 30.5], [10.0, 25.3], [5.5, 15.8], ]

pentagon = [[15.4, 40.2], [20.1, 30.5], [10.0, 25.3], [5.5, 15.8], [8.2, 35.1], [15.4, 40.2]]

# 2. Multi-polygon (pětiúhelník + čtverec)
square = [[0.0, 0.0], [10.0, 0.0], [10.0, 10.0], [0.0, 10.0], [0.0, 0.0]]
multi_polygon = [pentagon, square]

# 3. Druhý vrchol prvního polygonu (indexování)
second_vertex = multi_polygon[0][1]

# 4. Poslední tři vrcholy druhého polygonu pozpátku (slicing)
last_three_reversed = multi_polygon[1][-4:-1][::-1]

print("Pětiúhelník:", pentagon)
print("Multi-polygon:", multi_polygon)
print("Druhý vrchol prvního polygonu:", second_vertex)
print("Poslední tři vrcholy druhého polygonu pozpátku:", last_three_reversed)
print("Původní seznam:", polygon)

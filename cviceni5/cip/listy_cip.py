# listy_cip.py - Cvičení 5: Seznamy (Lists)

# ============================================================================
# ÚKOL 1: Definice seznamů a výběr prvků (Blok L6-1)
# ============================================================================

print("=" * 70)
print("ÚKOL 1: Definice seznamů a výběr prvků")
print("=" * 70)

# 1. Vytvořte seznam souřadnic reprezentující pětiúhelník
# Pětiúhelník = 5 vrcholů + opakovaný první bod pro uzavření
pentagon = [
    [14.4, 50.1],   # Bod 1
    [14.6, 50.2],   # Bod 2
    [14.7, 49.9],   # Bod 3
    [14.5, 49.8],   # Bod 4
    [14.3, 49.9],   # Bod 5
    [14.4, 50.1]    # Opakovaný první bod pro uzavření polygonu
]
print(f"\n1. Pětiúhelník:\n{pentagon}")

# 2. Vytvořte čtverec (druhý polygon)
square = [
    [15.0, 50.5],   # Bod 1
    [15.2, 50.5],   # Bod 2
    [15.2, 50.3],   # Bod 3
    [15.0, 50.3],   # Bod 4
    [15.0, 50.5]    # Opakovaný první bod
]
print(f"\n2. Čtverec:\n{square}")

# 3. Vytvořte multi-polygon (seznam obsahující oba polygony)
multi_polygon = [pentagon, square]
print(f"\n3. Multi-polygon (seznam obou polygonů):\n{multi_polygon}")

# 4. Indexování: získejte druhý vrchol prvního polygonu
second_vertex = multi_polygon[0][1]  # První polygon [0], druhý vrchol [1]
print(f"\n4. Druhý vrchol prvního polygonu (indexování):\n   {second_vertex}")

# 5. Slicing: získejte poslední tři vrcholy druhého polygonu seřazené pozpátku
last_three_vertices = multi_polygon[1][-3:][::-1]  # Poslední 3 [:−3:], obráceno [::-1]
print(f"\n5. Poslední tři vrcholy druhého polygonu seřazené pozpátku:\n   {last_three_vertices}")

# ============================================================================
# ÚKOL 2: Metody a funkce (Blok L6-2)
# ============================================================================

print("\n" + "=" * 70)
print("ÚKOL 2: Metody a funkce")
print("=" * 70)

# 1. Vytvořte seznam bodů reprezentující trasu (alespoň 4 body)
route = [
    [14.4, 50.0],   # Bod 1
    [14.5, 50.1],   # Bod 2
    [14.6, 50.2],   # Bod 3
    [14.7, 50.3]    # Bod 4
]
print(f"\n1. Původní trasa (4 body):\n   {route}")

# 2. Přidejte nový bod na konec pomocí append
new_point = [14.8, 50.4]
route.append(new_point)
print(f"\n2. Trasa po přidání bodu na konec (append):\n   {route}")

# 3. Vložte bod doprostřed trasy pomocí insert
middle_point = [14.55, 50.15]
route.insert(len(route) // 2, middle_point)  # Vložení uprostřed
print(f"\n3. Trasa po vložení bodu uprostřed (insert):\n   {route}")

# 4. Vytvořte nový seznam bodů seřazených podle lat (y-souřadnice)
sorted_route = sorted(route, key=lambda point: point[1])
print(f"\n4. Trasa seřazená podle lat (y-souřadnice):\n   {sorted_route}")

# 5. Spočítejte průměrnou lon a lat souřadnici všech bodů
avg_lon = sum(point[0] for point in route) / len(route)
avg_lat = sum(point[1] for point in route) / len(route)
print(f"\n5. Průměrné souřadnice trasy:")
print(f"   Průměrná lon: {avg_lon:.4f}")
print(f"   Průměrná lat: {avg_lat:.4f}")

# ============================================================================
# ÚKOL 3: Pokročilé procházení a list comprehension (Blok L6-3)
# ============================================================================

print("\n" + "=" * 70)
print("ÚKOL 3: Pokročilé procházení a list comprehension")
print("=" * 70)

# 1. Vytvořte seznam souřadnic [lon, lat, výška] — výškový profil trasy
elevation_profile = [
    [14.4, 50.0, 320],    # Bod 1: výška 320 m
    [14.5, 50.1, 350],    # Bod 2: výška 350 m
    [14.6, 50.2, 380],    # Bod 3: výška 380 m
    [14.7, 50.3, 365],    # Bod 4: výška 365 m
    [14.8, 50.4, 340]     # Bod 5: výška 340 m
]
print(f"\n1. Výškový profil trasy (5 bodů):\n   {elevation_profile}")

# 2. Projděte body pomocí enumerate a vypište zprávu
print("\n2. Průchod body s enumerate:")
for index, point in enumerate(elevation_profile, start=1):
    lon, lat, elevation = point
    print(f"   Bod {index}: výška {elevation} m n. m.")

# 3. Spočítejte průměrnou nadmořskou výšku
elevations = [point[2] for point in elevation_profile]
avg_elevation = sum(elevations) / len(elevations)
print(f"\n3. Průměrná nadmořská výška: {avg_elevation:.1f} m n. m.")

# 4. List comprehension: body s výškou větší než průměr
above_average = [point for point in elevation_profile if point[2] > avg_elevation]
print(f"\n4a. Body s výškou větší než průměr ({avg_elevation:.1f} m):")
for point in above_average:
    print(f"    {point}")

# 4. List comprehension: seznam obsahující pouze výšky
heights_only = [point[2] for point in elevation_profile]
print(f"\n4b. Seznam obsahující pouze výšky (bez souřadnic):")
print(f"    {heights_only}")

# Bonus: vypočítejte výškový rozdíl (gain/loss)
elevation_gain = sum(max(0, elevations[i+1] - elevations[i]) for i in range(len(elevations)-1))
elevation_loss = sum(max(0, elevations[i] - elevations[i+1]) for i in range(len(elevations)-1))
print(f"\n5. Bonusové statistiky:")
print(f"   Převýšení (gain): {elevation_gain} m")
print(f"   Pokles (loss): {elevation_loss} m")
print(f"   Minimální výška: {min(heights_only)} m n. m.")
print(f"   Maximální výška: {max(heights_only)} m n. m.")

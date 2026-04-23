city = "Olomouc"
coord = [49.1951, 16.6068]
population = 100000
area = 103.3
is_capital_city = False

# hustota zalidnění
hustota_zalidneni = population / area

print(type(city))
print(type(coord))
print(type(population))
print(type(area))
print(type(is_capital_city))

jmeno = input("Jaké je tvé jméno? ")
print(f"Ahoj {jmeno}, město {city} má hustotu {hustota_zalidneni} obyv./km² a nachází se na souřadnicích {coord}.")
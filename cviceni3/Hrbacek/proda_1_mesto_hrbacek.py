city = "Ostrava"
souradnice = [49.8346453, 18.2820442]
pocet_obyvatel = 283000
rozloha = 214.23
hlavni_mesto = False

hustota = pocet_obyvatel / rozloha
print(hustota)

print(type(city))
print(type(souradnice))
print(type(pocet_obyvatel))
print(type(rozloha))
print(type(hlavni_mesto))
print(type(hustota))

jmeno = input("Jak se jmenuješ? ")
print(f"Ahoj {jmeno}, město {city} má hustotu {hustota:.2f} obyv./km² a nachází se na souřadnicích {souradnice}.")
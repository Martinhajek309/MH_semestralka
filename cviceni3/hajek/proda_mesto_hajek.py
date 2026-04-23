
nazev_mesta = "Praha"
souradnice = [50.0755, 14.4378]
pocet_obyvatel = 1300000
rozloha_km2 = 496.21
je_hlavni_mesto = True

hustota_zalidneni = pocet_obyvatel / rozloha_km2

print(type(nazev_mesta))
print(type(souradnice))
print(type(pocet_obyvatel))
print(type(rozloha_km2))
print(type(je_hlavni_mesto))

jmeno = input("Zadej své jméno: ")

print(f"Ahoj {jmeno}, město {nazev_mesta} má hustotu {hustota_zalidneni:.2f} obyv./km² a nachází se na souřadnicích {souradnice}.")

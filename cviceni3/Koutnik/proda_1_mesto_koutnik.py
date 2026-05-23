nazev_mesta = "Olomouc"
souradnice = [49.5938, 17.2509]  
pocet_obyvatel = 101825          
rozloha_km2 = 103.33             
je_hlavni_mesto = False          


hustota_zalidneni = pocet_obyvatel / rozloha_km2

print("--- Typy proměnných ---")
print(f"nazev_mesta: {type(nazev_mesta)}")
print(f"souradnice: {type(souradnice)}")
print(f"pocet_obyvatel: {type(pocet_obyvatel)}")
print(f"rozloha_km2: {type(rozloha_km2)}")
print(f"je_hlavni_mesto: {type(je_hlavni_mesto)}")
print(f"hustota_zalidneni: {type(hustota_zalidneni)}")
print("-" * 20)

jmeno_uzivatele = input("Jak se jmenuješ? ")


print(f"Ahoj {jmeno_uzivatele}, město {nazev_mesta} má hustotu {hustota_zalidneni:.2f} obyv./km² a nachází se na souřadnicích {souradnice}.")
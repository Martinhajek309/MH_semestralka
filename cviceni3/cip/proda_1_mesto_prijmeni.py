

# Definice proměnných pro oblíbené město (příklad: Praha)
nazev_mesta = "Praha"  # str - název města
souradnice = [50.0755, 14.4378]  # list - šířka a délka
pocet_obyvatel = 1309000  # int - počet obyvatel
rozloha_km2 = 496.0  # float - rozloha v km²
je_hlavnim_mestem = True  # bool - zda je hlavním městem

# Výpočet hustoty zalidnění
hustota_zalidneni = pocet_obyvatel / rozloha_km2

# Výpis typů proměnných
print("Typy proměnných:")
print(f"nazev_mesta: {type(nazev_mesta)}")
print(f"souradnice: {type(souradnice)}")
print(f"pocet_obyvatel: {type(pocet_obyvatel)}")
print(f"rozloha_km2: {type(rozloha_km2)}")
print(f"je_hlavnim_mestem: {type(je_hlavnim_mestem)}")
print(f"hustota_zalidneni: {type(hustota_zalidneni)}")

# Zeptej se na jméno uživatele
jmeno = input("Zadejte vaše jméno: ")

# Výpis pomocí f-stringu
print(f"Ahoj {jmeno}, město {nazev_mesta} má hustotu {hustota_zalidneni:.2f} obyv./km² a nachází se na souřadnicích {souradnice}.")

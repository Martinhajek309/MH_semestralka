nazev_mesta = "Olomouc"
souradnice = (49.5938, 17.2509)
pocet_obyvatel = 101000
rozloha_km2 = 103.36
is_captial = False

pop_density = pocet_obyvatel / rozloha_km2

# zeptáme se uživatele na jméno
user_name = input("Zadej své jméno: ")

# vypíšeme informaci formátovanou f-stringem
print(f"Ahoj {user_name}, město {nazev_mesta} má hustotu {pop_density:.2f} obyv./km² a nachází se na souřadnicích {souradnice}.")

# původní výpis typů proměnných (ponecháme pro kontrolu)
print("typ nazev_mesta:", type(nazev_mesta))
print("typ souradnice:", type(souradnice))
print("typ pocet_obyvatel:", type(pocet_obyvatel))
print("typ rozloha_km2:", type(rozloha_km2))
print("typ is_captial:", type(is_captial))
print("typ pop_density:", type(pop_density))
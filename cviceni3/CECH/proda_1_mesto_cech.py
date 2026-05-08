# úkol 1

city_name = "Tokio"
city_coordinates = [35.6895, 139.6917]
pocet_obyvatel = 13929286
rozloha = 2191
hl_mesto = True

hustota_obyvatel = pocet_obyvatel / rozloha

print("Hustota obyvatel je", hustota_obyvatel, "obyvatel na km^2.")

print(
    "Typy proměnných: Název města:", type(city_name),
    "Souřadnice:", type(city_coordinates),
    "Počet obyvatel:", type(pocet_obyvatel),
    "Rozloha:", type(rozloha),
    "Status hlavního města:", type(hl_mesto)
)

jmeno_uzivatele = input("Zadejte své jméno: ")

print(
    f"Ahoj {jmeno_uzivatele}, město {city_name} má hustotu "
    f"{hustota_obyvatel:.2f} obyv./km² a nachází se na souřadnicích {city_coordinates}."
)
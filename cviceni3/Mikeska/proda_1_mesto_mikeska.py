# Úkol 1: Proměnné a datové typy

mesto = "Praha"
souradnice = [50.0755, 14.4378]
pocet_obyvatel = 1386429
rozloha_km2 = 496.0
je_hlavni_mesto = True

hustota_zalidneni = pocet_obyvatel / rozloha_km2

print(type(mesto))
print(type(souradnice))
print(type(pocet_obyvatel))
print(type(rozloha_km2))
print(type(je_hlavni_mesto))
print(type(hustota_zalidneni))

jmeno = input("Zadejte své jméno: ")

print(
    f"Ahoj {jmeno}, město {mesto} má hustotu {hustota_zalidneni:.2f} obyv./km² "
    f"a nachází se na souřadnicích {souradnice}."
)
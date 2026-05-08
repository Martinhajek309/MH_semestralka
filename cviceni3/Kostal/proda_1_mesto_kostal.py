"""Zakladni prace s promennymi a datovymi typy."""

# Udaje o oblibenem meste.
mesto = "Olomouc"
souradnice = [49.5938, 17.2509]
pocet_obyvatel = 100663
rozloha_km2 = 103.36
je_hlavni_mesto = False

# Vypocet hustoty zalidneni.
hustota_zalidneni = pocet_obyvatel / rozloha_km2

# Vypsani datovych typu jednotlivych promennych.
print(f"Typ promenne mesto: {type(mesto)}")
print(f"Typ promenne souradnice: {type(souradnice)}")
print(f"Typ promenne pocet_obyvatel: {type(pocet_obyvatel)}")
print(f"Typ promenne rozloha_km2: {type(rozloha_km2)}")
print(f"Typ promenne je_hlavni_mesto: {type(je_hlavni_mesto)}")

# Nacteni jmena uzivatele a vytvoreni vystupni vety pomoci f-stringu.
jmeno = input("Zadej sve jmeno: ")
print(
    f"Ahoj {jmeno}, mesto {mesto} ma hustotu "
    f"{hustota_zalidneni:.2f} obyv./km2 a nachazi se na souradnicich {souradnice}."
)

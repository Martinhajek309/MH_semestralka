nazev_mesta = "Ostrava"
souradnice = [49.8209, 18.2625]
pocet_obyvatel = 290000
rozloha = 214.23
hlavni_mesto = False

hustota_zalidneni = pocet_obyvatel / rozloha

print(f"Typ promenne nazev_mesta: {type(nazev_mesta)}")
print(f"Typ promenne souradnice: {type(souradnice)}")
print(f"Typ promenne pocet_obyvatel: {type(pocet_obyvatel)}")
print(f"Typ promenne rozloha: {type(rozloha)}")
print(f"Typ promenne hlavni_mesto: {type(hlavni_mesto)}")

jmeno_uzivatele = input("Zadejte sve jmeno: ")

print(
    f"Ahoj {jmeno_uzivatele}, mesto {nazev_mesta} ma hustotu "
    f"{hustota_zalidneni:.2f} obyv./km2 a nachazi se na souradnicich {souradnice}."
)

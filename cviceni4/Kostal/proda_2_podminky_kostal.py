"""Klasifikace pocasi podle teploty a vlhkosti."""

teplota = float(input("Zadej aktualni teplotu ve stupnich Celsia: "))
vlhkost = float(input("Zadej aktualni vlhkost v procentech: "))

if vlhkost < 0 or vlhkost > 100:
    print("Chyba: Neplatna hodnota vlhkosti!")
else:
    if teplota < 0:
        print("Mrzne")
    elif 0 <= teplota <= 10:
        print("Je zima")
    elif 10 < teplota <= 25:
        print("Je mirne pocasi")
    else:
        print("Je teplo")

    if teplota > 25 and vlhkost > 70:
        print("Pozor na tropicke vedro!")

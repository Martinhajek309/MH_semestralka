# úkol 2
aktualni_teplota = float(input("Zadejte aktuální teplotu v Celsiích: "))
aktualni_vlhkost = float(input("Zadejte aktuální vlhkost v procentech: "))

if aktualni_vlhkost < 0 or aktualni_vlhkost > 100:
    print("Chyba: Neplatná hodnota vlhkosti!")
else:
    if aktualni_teplota < 0:
        print("Mrzne")
    elif aktualni_teplota <= 10:
        print("Je zima")
    elif aktualni_teplota < 25:
        print("Je mírné počasí")
    else:
        print("Je teplo")

    if aktualni_teplota > 25 and aktualni_vlhkost > 70:
        print("Pozor na tropické vedro!")

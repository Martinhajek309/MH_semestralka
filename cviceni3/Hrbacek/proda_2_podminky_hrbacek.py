teplota = float(input("Zadej aktuální teplotu (°C): "))
vlhkost = float(input("Zadej vlhkost (%): "))

if vlhkost < 0 or vlhkost > 100:
    print("Chyba: Neplatná hodnota vlhkosti!")
else:
    if teplota < 0:
        print("Mrzne")
    elif 0 <= teplota <= 10:
        print("Je zima")
    elif 10 < teplota <= 25:
        print("Je mírné počasí")
    else:
        print("Je teplo")
    if teplota > 25 and vlhkost > 70:
        print("Pozor na tropické vedro!")
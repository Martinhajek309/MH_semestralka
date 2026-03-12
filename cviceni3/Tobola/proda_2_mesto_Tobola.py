teplota = int(input("Zadat teplotu"))
vlhkost = int(input("Zadat vlhkost "))

if vlhkost < 0 or vlhkost > 100:
    print("Chyba - zadány nesprávné hodnoty")
else:
    if teplota < 0:
        print("Mrzne")
    elif 0 <= teplota <= 10:
        print("Je zima")
    elif 10 < teplota <= 25:
        print("Je mírné počasí")
    else:
        print("Je teplo")

    # Vedro
    if teplota > 25 and vlhkost > 70:
        print("Pozor na tropické vedro!")
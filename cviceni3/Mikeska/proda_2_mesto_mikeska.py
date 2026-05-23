teplota = float(input("Zadejte teplotu v °C: "))
vlhkost = float(input("Zadejte vlhkost v %: "))

if teplota < 0:
    print("Mrzne")
elif teplota <= 10:
    print("Je zima")
elif teplota <= 25:
    print("Je mírné počasí")
else:
    print("Je teplo")

if vlhkost < 0 or vlhkost > 100:
    print("Chyba: Neplatná hodnota vlhkosti!")
elif teplota > 25 and vlhkost > 70:
    print("Pozor na tropické vedro!")
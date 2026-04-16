teplota = float(input("aktuální teplota"))
vlhkost = float(input("aktuální vlhkost"))
if 0 > vlhkost or vlhkost > 100:
      print("Chyba: Neplatná hodnota vlhkosti!")
elif teplota < 0:
     print("Mrzne")
elif 0 <= teplota <= 10:
    print("Je zima") 
elif 10 <= teplota <= 25:
    print("Je mírné počasí")
elif 25 <= teplota:
        print("Je teplo")
if 25 <= teplota and vlhkost >= 70:
        print("Pozor na tropické vedro!")


    
aktualni_teplota = float(input("Zadejte aktuální teplotu: ")) 
vlhkost_vzduchu = float(input("Zadejte vlhkost vzduchu: "))


if vlhkost_vzduchu < 0 or vlhkost_vzduchu > 100:
        print("Neplatná hodnota vlhkosti vzduchu!")
else:
    if aktualni_teplota < 0:
        print("Mrzne.")
    elif aktualni_teplota >= 0 and aktualni_teplota <= 10:
        print("Je zima.")
    elif aktualni_teplota > 10 and aktualni_teplota < 25:
        print("Je mírné počasí.")
    else:
        print("Je teplo.")

    if aktualni_teplota > 25 and vlhkost_vzduchu > 70:
        print("Pozor na tropické vedro!")
    
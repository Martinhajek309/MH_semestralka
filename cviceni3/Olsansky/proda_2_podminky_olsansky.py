teplota = int(input("Zadejte teplotu (pouze číslo): "))
vlhkost = int(input("Zadejte vlhkost (pouze číslo): ")) 

if vlhkost < 0 or vlhkost > 100:
    print("Neplatná vlhkost. Zadejte hodnotu mezi 0 a 100.")
else:
    if teplota < 0:
        print("Mrzne.")
    elif teplota >= 0 and teplota <= 10:
        print("Je zima.")
    elif teplota > 10 and teplota <= 25:
        print("Je mírné počasí.")
    elif teplota > 25:
        print("Je teplo.")

    if vlhkost > 75 and teplota > 25:
        print("Pozor na troické vedro.")
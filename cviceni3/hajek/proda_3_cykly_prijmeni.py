mereni = [12.5, 13.2, 14.0, 15.1, 16.3, 55.0, 17.8, 18.4, 19.0, 20.2, -25.0, 21.5]
pocet_platnych = 0

for hodina, teplota in enumerate(mereni):
    if teplota > 50:
        print(f"Hodina {hodina}:00: Nesmyslná hodnota (káva na senzoru), přeskakuji.")
        continue
    elif teplota < -20:
        print(f"Hodina {hodina}:00: Kritická chyba senzoru, ukončuji kontrolu!")
        break
    else:
        print(f"Teplota v {hodina}:00 byla {teplota}°C.")
        pocet_platnych += 1

print(f"Počet platných zpracovaných měření: {pocet_platnych}")
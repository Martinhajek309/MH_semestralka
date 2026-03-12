mereni = [12.5, 13.2, 55.0, 14.1, -25.0, 52.3, -12.3, 10.0, 25.3, -5.6, 5.6, 2.1, 66.6, 15.2, 16.1, 15.2, 99.9, -99.9, 24.4, 12.5, 13.2, 55.0, 14.1, -25.0,]

for hodina, teplota in enumerate(mereni):
    if teplota > 50:
        print(f"Hodina {hodina}:00: Nesmyslná hodnota (káva na senzoru), přeskakuji.")
        continue
    if teplota < -20:
        print(f"Hodina {hodina}:00: Kritická chyba senzoru, ukončuji kontrolu!")
        break

    print(f"Teplota v {hodina}:00 byla {teplota}°C.")
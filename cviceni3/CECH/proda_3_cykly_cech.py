# úkol 3

seznam = [12.5, 13.2, 55.0, 14.1, -25.0, 8.0, 0.9, 22.2, 17.7, 3.2, 9.1, 3.6, 9.9, -22.4, 11.0, 5.5, 6.3, 4.4, 7.8, 60.0, 10.5]
pocet_pl_mereni = 0

for i, hodnota in enumerate(seznam):

    if hodnota > 50:
        print(f"Hodina {i}:00: Nesmyslná hodnota (káva na senzoru), přeskakuji.")
        continue

    elif hodnota < -20:
        print(f"Hodina {i}:00: Kritická chyba senzoru, ukončuji kontrolu!")
        break

    else:
        print(f"Hodina měření: {i}:00, hodnota: {hodnota}°C")
        print(f"Teplota v {i}:00 byla {hodnota}°C.")
        pocet_pl_mereni += 1

print("Počet platných měření:", pocet_pl_mereni)
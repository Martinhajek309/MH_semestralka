mereni = [12.5, 13.2, 14.1, 15.0, 55.0, 16.3, 17.8, -5.0, 18.2, -25.0, 19.1, 20.0]

platna_mereni = 0

for index, hodnota in enumerate(mereni):

    if hodnota > 50:
        print(f"Hodina {index}:00: Nesmyslná hodnota (káva na senzoru), přeskakuji.")
        continue

    if hodnota < -20:
        print(f"Hodina {index}:00: Kritická chyba senzoru, ukončuji kontrolu!")
        break

    print(f"Teplota v {index}:00 byla {hodnota}°C.")
    platna_mereni += 1

print(f"Počet platných měření: {platna_mereni}")
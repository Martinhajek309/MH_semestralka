mereni = [12.5, 13.2, 55.0, 14.1, -25.0, 53.0, 12.30, 14.0, 15.5, 16.0, -34.0, 17.5, 18.0, 19.0, 20.0, -16.0, 21.5, 22.0, 23.0, 24.0]

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
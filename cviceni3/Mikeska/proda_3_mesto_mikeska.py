# proda_3_cykly_prijmeni.py

mereni = [12.5, 13.2, 55.0, 14.1, -25.0, 15.8, 16.2, 18.4, 51.3, 17.0, 19.6, 20.1, 21.0, -19.5]

zpracovano = 0

for hodina, teplota in enumerate(mereni):
    if teplota > 50:
        print(f"Hodina {hodina}:00: Nesmyslná hodnota (káva na senzoru), přeskakuji.")
        continue
    if teplota < -20:
        print(f"Hodina {hodina}:00: Kritická chyba senzoru, ukončuji kontrolu!")
        break

    print(f"Teplota v {hodina}:00 byla {teplota}°C.")
    zpracovano += 1

print(f"Úspěšně zpracováno platných měření: {zpracovano}")
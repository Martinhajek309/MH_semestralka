"""Zpracovani mereni z meteostanice pomoci cyklu."""

mereni = [12.5, 13.2, 15.0, 18.4, 55.0, 14.1, 16.8, 19.3, 11.7, 8.6, -25.0, 7.9]
platna_mereni = 0

for hodina, teplota in enumerate(mereni):
    if teplota > 50:
        print(
            f"Hodina {hodina}:00: Nesmyslna hodnota "
            "(kava na senzoru), preskakuji."
        )
        continue

    if teplota < -20:
        print(f"Hodina {hodina}:00: Kriticka chyba senzoru, ukoncuji kontrolu!")
        break

    print(f"Teplota v {hodina}:00 byla {teplota}°C.")
    platna_mereni += 1

print(f"Uspesne bylo zpracovano {platna_mereni} platnych mereni.")

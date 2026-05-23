mereni = [12.5, 13.2, 55.0, 14.1, 15.0, 16.2, 17.5, 18.0, 15.5, -25.0, 114.0, 13.0]
platna_mereni = 0

for hodina, teplota in enumerate(mereni):
    if teplota > 50:
        print(f"Hodina {hodina}:00: Nesmyslná hodnota (káva na senzoru), přeskakuji.")
        continue
    
    if teplota < -20:
        print(f"Hodina {hodina}:00: Kritická chyba senzoru, ukončuji kontrolu!")
        break
    
    print(f"Teplota v {hodina}:00 byla {teplota}°C.")
    platna_mereni += 1

print("-" * 20)
print(f"Úspěšně zpracováno {platna_mereni} platných měření.")
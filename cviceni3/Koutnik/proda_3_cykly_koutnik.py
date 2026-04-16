mereni = [12.5, 13.2, 55.0, 14.1, 15.5, 16.0, 14.8, 13.9, -25.0, 12.0, 11.5, 10.8]
platna_mereni_count = 0
for i, teplota in enumerate(mereni):    
    if teplota > 50:
        print(f"Hodina {i}:00: Nesmyslná hodnota (káva na senzoru), přeskakuji.")
        continue
    if teplota < -20:
        print(f"Hodina {i}:00: Kritická chyba senzoru, ukončuji kontrolu!")
        break 
    print(f"Teplota v {i}:00 byla {teplota}°C.")
    platna_mereni_count += 1

print("-" * 30)
print(f"Celkem bylo úspěšně zpracováno {platna_mereni_count} platných měření.")
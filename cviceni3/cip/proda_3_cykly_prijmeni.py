# Cvičení 3: Cykly s continue a break
# Práce s měřením teploty a zpracováním chyb

# 1. VYTVOŘENÍ SEZNAMU MĚŘENÍ (alespoň 12 hodnot)
# Obsahuje chyby: hodnoty nad 50°C a pod -20°C
mereni = [12.5, 13.2, 55.0, 14.1, -25.0, 18.3, 52.7, 16.4, 19.8, 15.2, -22.5, 20.1, 21.5, 14.9]

# 2. INICIALIZACE PROMĚNNÉ PRO POČÍTADLO PLATNÝCH MĚŘENÍ
pocet_platnych = 0

# 3. CYKLUS: projdeme seznam měření se VSTUPY a INDEXEM
print("=== Kontrola měření teploty ===\n")

for index, teplota in enumerate(mereni):
    # Vypočítáme hodinu - index 0 = 0:00, index 1 = 1:00, atd.
    hodina = index
    
    # LOGIKA: Kontrola teploty
    
    # Pokud je teplota nad 50°C → nesmyslná hodnota
    if teplota > 50:
        print(f"Hodina {hodina}:00: Nesmyslná hodnota (káva na senzoru), přeskakuji.")
        continue  # Skočíme na další iteraci cyklu, toto měření se nepočítá
    
    # Pokud je teplota pod -20°C → kritická chyba
    if teplota < -20:
        print(f"Hodina {hodina}:00: Kritická chyba senzoru, ukončuji kontrolu!")
        break  # Ukončíme cyklus úplně
    
    # Pokud je teplota v pořádku
    print(f"Teplota v {hodina}:00 byla {teplota}°C.")
    pocet_platnych += 1  # Zvýšíme počítadlo platných měření

# 4. SHRNUTÍ: Výpis počtu zpracovaných měření
print(f"\n=== Shrnutí ===")
print(f"Úspěšně zpracováno {pocet_platnych} platných měření.")

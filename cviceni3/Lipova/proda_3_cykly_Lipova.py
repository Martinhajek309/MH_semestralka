seznam_mereni = [12.5, 13.2, 55.0, 23.1, 8.9, 55.0, -26.0, 0.0, 100.0, 75.5, 42.0, 55.4, 60.2, 10.0]
pocet_platnych_mereni = 0
for i, hodnota in enumerate(seznam_mereni):
    
    if seznam_mereni[i] > 50:
        print(f"Hodina {i}:00: Nesmyslná hodnota (káva na senzoru), přeskakuji.")
        continue
    elif seznam_mereni[i] < -20:
            print(f"Hodina {i}:00: Kritická chyba senzoru, ukončuji kontrolu.")
            break
    else:
        print(f"teplota v {i}:00 byla {seznam_mereni[i]}°C.")
        pocet_platnych_mereni += 1
print("Počet platných měření: " + str(pocet_platnych_mereni))




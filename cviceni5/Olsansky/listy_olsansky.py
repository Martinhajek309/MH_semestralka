# ukol 1
souradnice = [[10, 10], [11, 11], [11, 12], [10, 13], [9, 12], [9, 11], [10, 10]] #souradnice petiuhelniku
multipolygon = [souradnice, [[20, 20], [20, 21], [21, 21], [21, 20], [20, 20]]] #multipolygon obsahuje puvodni petiuhelnik a nový čtverec
druhy_vrchol = multipolygon[0][1] #druhy vrchol z prvního polygonu (petiuhelníku)
posledni_tri_vrcholy = multipolygon[1][5:1:-1] #poslední tři vrcholy z druhého polygonu (čtverce) serazene po zpatku
# ukol 2
trasa_souradnice = [[10, 10], [11, 11], [11, 12], [10, 13], [9, 12], [9, 11], [10, 10]]
trasa_souradnice.append([20, 20]) #pridani noveho vrcholu do trasy
trasa_souradnice.insert(0, [15, 15]) #pridani noveho vrcholu na zacatek trasy
sorted_trasa = sorted(trasa_souradnice, key=lambda x: x[1]) #serazeni souradnic trasy podle y hodnot
length_trasa = len(trasa_souradnice) #zjisteni delky trasy
average_trasa = sum_trasa / length_trasa #vypocet prumeru souradnic trasy
# ukol 3
trasa2_souradnice = [[20, 20, 435], [21, 21, 438], [21, 22, 500], [22, 23, 515], [23, 23, 500]]
enum_souradnice = enumerate(trasa2_souradnice) #vytvoreni enumerace pro trasa2_souradnice
sum_vysky = sum([x[2] for x in trasa2_souradnice]) #secteni vysky pro vsechny souradnice v trasa2
average_vyska = sum_vysky / len(trasa2_souradnice) #vypocet prumerne vysky pro trasa2
comprehension_trasy2_vyska_nad_prumerem = [x[2] for x in trasa2_souradnice if x[2] > average_vyska] #vytvoreni seznamu vysky pro souradnice v trasa2, ktere jsou nad prumernou vyskou
comprehension_trasy2_vyska_only = [x[2] for x in trasa2_souradnice] #vytvoreni seznamu vysky pro vsechny souradnice v trasa2

# vypis vysledku
print(f"Druhý vrchol: {druhy_vrchol}")
print(f"Poslední tři vrcholy: {posledni_tri_vrcholy}")
print(f"Seřazená trasa: {sorted_trasa}")
print(f"Průměr souřadnic trasy: {average_trasa}")
for cislo, souradnice in enum_souradnice:
    print(f"Bod {cislo}: výška {souradnice[2]} m n. m.")
print(f"Výšky nad průměrem: {comprehension_trasy2_vyska_nad_prumerem}")
print(f"Všechny výšky: {comprehension_trasy2_vyska_only}")
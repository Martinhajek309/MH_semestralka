petiuhelnik = [[0,0], [2,0], [3,2], [1,4], [-1,2], [0,0]]
ctverec = [[10, 10], [12, 10], [12, 12], [10, 12], [10, 10]]
multi_polygon = [petiuhelnik, ctverec]
print(f"Pětiúhelník: {petiuhelnik}")
print(f"Multi-polygon: {multi_polygon}")
druhy_vrchol = multi_polygon[0][1]
print(f"Druhý vrchol prvního polygonu: {druhy_vrchol}")
posledni_tri_zpetne = multi_polygon[1][-3:][::-1]
print(f"Poslední tři vrcholy čtverce pozpátku: {posledni_tri_zpetne}")

trasa = [
    [14.4, 50.1], 
    [14.5, 50.2], 
    [14.6, 50.0], 
    [14.7, 50.3]
]
trasa.append([14.8, 50.4])
trasa_serazena = sorted(trasa, key=lambda bod: bod[1])
vsechny_lon = [bod[0] for bod in trasa]
vsechny_lat = [bod[1] for bod in trasa]

prumerna_lon = sum(vsechny_lon) / len(vsechny_lon)
prumerna_lat = sum(vsechny_lat) / len(vsechny_lat)
print(f"Aktualizovaná trasa: {trasa}")
print(f"Trasa seřazená podle lat: {trasa_serazena}")
print(f"Průměrná souřadnice: [{prumerna_lon:.4f}, {prumerna_lat:.4f}]")

vyskovy_profil = [
    [14.2, 50.1, 250],
    [14.3, 50.2, 310],
    [14.4, 50.3, 450],
    [14.5, 50.4, 380],
    [14.6, 50.5, 520]
]
print("\n--- Výpis výškového profilu ---")
for i, bod in enumerate(vyskovy_profil):
    print(f"Bod {i + 1}: výška {bod[2]} m n. m.")

vsechny_vysky = [bod[2] for bod in vyskovy_profil]
prumerna_vyska = sum(vsechny_vysky) / len(vsechny_vysky)

nadprumerny_profil = [bod for bod in vyskovy_profil if bod[2] > prumerna_vyska]
jen_vysky = [bod[2] for bod in vyskovy_profil]
print(f"Průměrná výška: {prumerna_vyska} m n. m.")
print(f"Body s nadprůměrnou výškou: {nadprumerny_profil}")
print(f"Seznam samotných výšek: {jen_vysky}")
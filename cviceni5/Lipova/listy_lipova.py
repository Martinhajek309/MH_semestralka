import json

def vypocitej_vzdalenost_od_rovniku(sirka: float, jednotka: str = "km", zaokrouhlit: bool = False) -> float:
    vzdalenost = sirka * 111.32
    if jednotka == "mi":
        vzdalenost *= 0.621371
    if zaokrouhlit:
        vzdalenost = round(vzdalenost)
    return vzdalenost

def vytvor_geojson_bod(nazev: str, lat: float, lon: float) -> str:
    vzdal = vypocitej_vzdalenost_od_rovniku(lat)
    data = {
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [lon, lat]},
        "properties": {"nazev": nazev, "vzdalenost_od_rovniku": vzdal}
    }
    return json.dumps(data)

def prevod(hodnota: float, smer: str) -> float:
    if smer == "km_to_mi":
        return hodnota * 0.621371
    elif smer == "mi_to_km":
        return hodnota * 1.60934
    return 0.0

def pridej_bod(lat: float, lon: float, seznam_bodu: list) -> list:
    seznam_bodu.append([lat, lon])
    return seznam_bodu


trasa = [[14.4, 50.1], [14.5, 50.2], [14.6, 50.0], [14.7, 50.3]]
trasa.append([14.8, 50.4])


trasa.insert(2, [14.55, 50.15])

vsechny_lon = [bod[0] for bod in trasa]
vsechny_lat = [bod[1] for bod in trasa]
prumerna_lon = sum(vsechny_lon) / len(vsechny_lon)
prumerna_lat = sum(vsechny_lat) / len(vsechny_lat)


vyskovy_profil = [[14.2, 50.1, 250], [14.3, 50.2, 310], [14.4, 50.3, 450], [14.5, 50.4, 380], [14.6, 50.5, 520]]
vsechny_vysky = [bod[2] for bod in vyskovy_profil]
prumerna_vyska = sum(vsechny_vysky) / len(vsechny_vysky)
nadprumerny_profil = [bod for bod in vyskovy_profil if bod[2] > prumerna_vyska]


print(f"Trasa s insertem: {trasa}")
print(f"Průměr: [{prumerna_lon:.4f}, {prumerna_lat:.4f}]")
print(f"Nadprůměrné výšky: {nadprumerny_profil}")
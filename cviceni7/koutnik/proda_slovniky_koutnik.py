import copy
import json

poi_1 = {
    "ID": 1,
    "název": "Restaurace U Vlka",
    "souřadnice": (50.0755, 14.4378),
    "typ": "restaurace",
    "otevírací_hodiny": {
        "Po-Pá": "10:00-22:00",
        "So-Ne": "11:00-23:00"
    }
}

print("--- Úkol 1.2: Detail bodu zájmu ---")
for klic, hodnota in poi_1.items():
    print(f"{klic}: {hodnota}")

seznam_poi = [
    poi_1,
    {
        "ID": 2,
        "název": "Hrad Loket",
        "souřadnice": (50.1869, 12.7538),
        "typ": "památka",
        "otevírací_hodiny": {"Po-Ne": "09:00-17:00"}
    },
    {
        "ID": 3,
        "název": "Kavárna Slavia",
        "souřadnice": (50.0812, 14.4131),
        "typ": "restaurace",
        "otevírací_hodiny": {"Po-Ne": "08:00-21:00"}
    },
    {
        "ID": 4,
        "název": "Karlův most",
        "souřadnice": (50.0865, 14.4114),
        "typ": "památka",
        "otevírací_hodiny": {"Nonstop": "00:00-24:00"}
    }
]

print("\n--- Úkol 1.3: Vyhledávání restaurací ---")
for poi in seznam_poi:
    if poi["typ"] == "restaurace":
        print(f"Nalezeno: {poi['název']}")

for i in range(1, len(seznam_poi), 2):
    seznam_poi[i]["hodnoceni"] = 5 - i

seznam_poi.sort(key=lambda x: x.get("hodnoceni", 0), reverse=True)

print("\n--- Úkol 1.5: Bezpečný výpis hodnocení ---")
for poi in seznam_poi:
    print(f"Bod: {poi['název']}, Hodnocení: {poi.get('hodnoceni', 'Neznámé')}")

slovnik_id = {poi["ID"]: poi for poi in seznam_poi if poi.get("hodnoceni", 0) > 3}

print("\n--- Úkol 2.1: Slovník ID (hodnocení > 3) ---")
print(slovnik_id)

print("\n--- Úkol 2.2: Ukázka kopírování ---")

melka_kopie = list(seznam_poi)
hluboka_kopie = copy.deepcopy(seznam_poi)

seznam_poi[0]["otevírací_hodiny"]["Po-Ne"] = "ZAVŘENO"

print(f"Původní seznam (změněno): {seznam_poi[0]['otevírací_hodiny']['Po-Ne']}")
print(f"Mělká kopie (změna se projevila): {melka_kopie[0]['otevírací_hodiny']['Po-Ne']}")
print(f"Hluboká kopie (zůstalo původní): {hluboka_kopie[0]['otevírací_hodiny']['Po-Ne']}")

soubor_json = "body_zajmu_PRIJMENI.json"
with open(soubor_json, "w", encoding="utf-8") as f:
    json.dump(seznam_poi, f, ensure_ascii=False, indent=4)

print(f"\n--- Úkol 2.3: Data byla uložena do souboru {soubor_json} ---")
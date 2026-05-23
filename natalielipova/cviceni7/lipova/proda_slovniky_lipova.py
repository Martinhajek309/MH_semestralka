import json
import copy

bod_zajmu = {
    "nazev": "Vacenovice",
    "id": 12345,
    "souradnice": (49.12345, 16.54321),
    "typ": "obec",
    "otevírací_doba": {
        "pondělí": "9:00-17:00",    
        "úterý": "9:00-17:00",
        "středa": "9:00-17:00",
        "čtvrtek": "9:00-17:00",    
        "pátek": "9:00-17:00",
        "sobota": "10:00-16:00",    
        "neděle": "zavřeno"
    }
    }
for klic, hodnota in bod_zajmu.items():
    print(f"{klic}: {hodnota}")

bod1 = {
    "nazev": "Milotice",
    "id": 123456,
    "souradnice": (49.54321, 16.12345),
    "typ": "restaurace",
    "otevírací_doba": {
        "pondělí": "9:00-17:00",    
        "úterý": "9:00-17:00",
        "středa": "9:00-17:00",
        "čtvrtek": "9:00-17:00",    
        "pátek": "9:00-17:00",
        "sobota": "10:00-19:00",    
        "neděle": "zavřeno"
    }
}
bod2 = {
    "nazev": "Hodonín", 
    "id": 1234567,
    "souradnice": (49.67890, 16.67890),     
    "typ": "muzeum",
    "otevírací_doba": { 
        "pondělí": "9:00-17:00",    
        "úterý": "9:00-17:00",
        "středa": "9:00-17:00",
        "čtvrtek": "9:00-17:00",    
        "pátek": "9:00-17:00",
        "sobota": "10:00-18:00",    
        "neděle": "zavřeno"
    }
}   
seznam_bodu = [bod_zajmu, bod1, bod2]
for bod in seznam_bodu:
    if bod["typ"] == "obec":
        print(f"Obec: {bod['nazev']}")

for i in range(len(seznam_bodu)):
    if i % 2 == 0:
        seznam_bodu[i]["hodnoceni"] = 4.8


seznam_bodu.sort(key=lambda x: x.get("hodnoceni", 0), reverse=True)
for bod in seznam_bodu:
    print(f"{bod['nazev']}: {bod.get('hodnoceni', 'nezname')}")

slovnik_id = {bod["id"]: bod for bod in seznam_bodu if bod.get("hodnoceni", 0) > 3}
print(slovnik_id)
for klic, hodnota in slovnik_id.items():
    print(f"ID: {klic}, Název: {hodnota['nazev']}")

melka_kopie = copy.copy(seznam_bodu)
hluboka_kopie = copy.deepcopy(seznam_bodu)

melka_kopie[0]["nazev"] = "Změněný název"
print("Původní seznam:")

print(f"originální název: {seznam_bodu[0]['nazev']}")
print(f"mělká kopie název: {melka_kopie[0]['nazev']}")
print(f"hluboká kopie název: {hluboka_kopie[0]['nazev']}")

soubor_json_lipova = "bodu_zajmu_Lipova.json"
with open(soubor_json_lipova, "w") as f:
    json.dump(seznam_bodu, f, ensure_ascii=False, indent=4)

print(f"Data byla uložena do souboru {soubor_json_lipova}.")

          
          





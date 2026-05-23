import json
from copy import deepcopy
from pathlib import Path


print("=== Ukol 1: Slovniky ===")

bod_zajmu = {
    "id": 1,
    "nazev": "Arcibiskupsky palac",
    "souradnice": (17.2518, 49.5952),
    "typ": "pamatka",
    "oteviraci_hodiny": {
        "pondeli": "09:00-17:00",
        "utery": "09:00-17:00",
        "streda": "09:00-17:00",
        "ctvrtek": "09:00-17:00",
        "patek": "09:00-17:00",
        "sobota": "10:00-18:00",
        "nedele": "10:00-18:00",
    },
}

for klic, hodnota in bod_zajmu.items():
    print(f"{klic}: {hodnota}")

body_zajmu = [
    bod_zajmu,
    {
        "id": 2,
        "nazev": "Long Story Short",
        "souradnice": (17.2545, 49.5945),
        "typ": "restaurace",
        "oteviraci_hodiny": {
            "pondeli": "11:00-22:00",
            "utery": "11:00-22:00",
            "streda": "11:00-22:00",
            "ctvrtek": "11:00-22:00",
            "patek": "11:00-23:00",
            "sobota": "11:00-23:00",
            "nedele": "11:00-21:00",
        },
    },
    {
        "id": 3,
        "nazev": "Botanicka zahrada",
        "souradnice": (17.2692, 49.6010),
        "typ": "park",
        "oteviraci_hodiny": {
            "pondeli": "08:00-18:00",
            "utery": "08:00-18:00",
            "streda": "08:00-18:00",
            "ctvrtek": "08:00-18:00",
            "patek": "08:00-18:00",
            "sobota": "09:00-18:00",
            "nedele": "09:00-18:00",
        },
        "bezbarierovy_pristup": True,
    },
    {
        "id": 4,
        "nazev": "Caffe Caesar",
        "souradnice": (17.2504, 49.5936),
        "typ": "restaurace",
        "oteviraci_hodiny": {
            "pondeli": "08:00-21:00",
            "utery": "08:00-21:00",
            "streda": "08:00-21:00",
            "ctvrtek": "08:00-21:00",
            "patek": "08:00-22:00",
            "sobota": "09:00-22:00",
            "nedele": "09:00-20:00",
        },
    },
]

hledany_typ = "restaurace"
print(f"\nBody zajmu typu '{hledany_typ}':")
for bod in body_zajmu:
    if bod["typ"] == hledany_typ:
        print(f"- {bod['nazev']}")

for index in range(1, len(body_zajmu), 2):
    body_zajmu[index]["hodnoceni"] = 3.5 + index * 0.4

body_zajmu.sort(key=lambda bod: bod.get("hodnoceni", 0), reverse=True)

print("\nSerazeny seznam bodu zajmu podle hodnoceni:")
for bod in body_zajmu:
    print(f"- {bod['nazev']}: {bod.get('hodnoceni', 'Nezname')}")

print("\nBezpecny vypis atributu 'bezbarierovy_pristup':")
for bod in body_zajmu:
    print(f"- {bod['nazev']}: {bod.get('bezbarierovy_pristup', 'Nezname')}")


print("\n=== Ukol 2: Pokrocile metody slovniku ===")

slovnik_bodu = {
    bod["id"]: bod
    for bod in body_zajmu
    if bod.get("hodnoceni", 0) > 3
}

print("Body s hodnocenim vyssim nez 3 prevedene na slovnik:")
for identifikator, bod in slovnik_bodu.items():
    print(f"- {identifikator}: {bod['nazev']}")

melka_kopie = body_zajmu.copy()
hluboka_kopie = deepcopy(body_zajmu)

body_zajmu[0]["oteviraci_hodiny"]["pondeli"] = "12:00-20:00"

print("\nPorovnani po zmene vnorenych dat:")
print(f"Original: {body_zajmu[0]['oteviraci_hodiny']['pondeli']}")
print(f"Melka kopie: {melka_kopie[0]['oteviraci_hodiny']['pondeli']}")
print(f"Hluboka kopie: {hluboka_kopie[0]['oteviraci_hodiny']['pondeli']}")

vystupni_soubor = Path(__file__).with_name("body_zajmu_kostal.json")
with vystupni_soubor.open("w", encoding="utf-8") as soubor:
    json.dump(body_zajmu, soubor, ensure_ascii=False, indent=2)

print(f"\nJSON byl ulozen do souboru: {vystupni_soubor.name}")

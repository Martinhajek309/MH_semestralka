import copy
import json

body_zajmu = [
    {
        "ID": 1,
        "nazev_bodu": "Olomoucky orloj",
        "souradnice": (17.2518, 49.5938),
        "typ": "pamatka",
        "oteviraci_hodiny": {
            "pondeli": "08:00-18:00",
            "utery": "08:00-18:00",
            "streda": "08:00-18:00",
            "ctvrtek": "08:00-18:00",
            "patek": "08:00-18:00",
            "sobota": "09:00-17:00",
            "nedele": "09:00-17:00"
        }
    },
    {
        "ID": 2,
        "nazev_bodu": "Restaurace U Morice",
        "souradnice": (17.2501, 49.5945),
        "typ": "restaurace",
        "oteviraci_hodiny": {
            "pondeli": "11:00-22:00",
            "utery": "11:00-22:00",
            "streda": "11:00-22:00",
            "ctvrtek": "11:00-22:00",
            "patek": "11:00-23:00",
            "sobota": "11:00-23:00",
            "nedele": "11:00-21:00"
        }
    },
    {
        "ID": 3,
        "nazev_bodu": "Kavarna Na rohu",
        "souradnice": (17.2487, 49.5921),
        "typ": "restaurace",
        "oteviraci_hodiny": {
            "pondeli": "07:00-19:00",
            "utery": "07:00-19:00",
            "streda": "07:00-19:00",
            "ctvrtek": "07:00-19:00",
            "patek": "07:00-20:00",
            "sobota": "08:00-20:00",
            "nedele": "08:00-18:00"
        }
    }
]

print("Vypis prvniho bodu zajmu:")
for klic, hodnota in body_zajmu[0].items():
    print(f"{klic}: {hodnota}")

hledany_typ = "restaurace"
print(f"\nBody typu '{hledany_typ}':")
for bod in body_zajmu:
    if bod["typ"] == hledany_typ:
        print(f"- {bod['nazev_bodu']} na souradnicich {bod['souradnice']}")

body_zajmu[1]["hodnoceni"] = 4.7

serazene_body = sorted(body_zajmu, key=lambda bod: bod.get("hodnoceni", 0), reverse=True)

print("\nSerazene body podle hodnoceni:")
for bod in serazene_body:
    print(f"{bod['nazev_bodu']} - hodnoceni: {bod.get('hodnoceni', 'Nezname')}")

print("\nBezpecny vypis hodnoceni:")
for bod in body_zajmu:
    print(f"{bod['nazev_bodu']} - hodnoceni: {bod.get('hodnoceni', 'Nezname')}")

slovnik_bodu = {
    bod["ID"]: bod
    for bod in body_zajmu
    if bod.get("hodnoceni", 0) > 3
}

print("\nSlovnik bodu s hodnocenim vyssim nez 3:")
for klic, hodnota in slovnik_bodu.items():
    print(f"{klic}: {hodnota}")

melka_kopie = body_zajmu[:]
hluboka_kopie = copy.deepcopy(body_zajmu)

melka_kopie[0]["oteviraci_hodiny"]["pondeli"] = "10:00-20:00"
hluboka_kopie[1]["oteviraci_hodiny"]["utery"] = "12:00-23:00"

print("\nPorovnani kopii:")
print("Original - 1. bod, pondeli:", body_zajmu[0]["oteviraci_hodiny"]["pondeli"])
print("melka kopie - 1. bod, pondeli:", melka_kopie[0]["oteviraci_hodiny"]["pondeli"])
print("Hluboka kopie - 2. bod, utery:", hluboka_kopie[1]["oteviraci_hodiny"]["utery"])
print("Original - 2. bod, utery:", body_zajmu[1]["oteviraci_hodiny"]["utery"])

with open("body_zajmu_CECH.json", "w", encoding="utf-8") as soubor:
    json.dump(body_zajmu, soubor, ensure_ascii=False, indent=4)

print("\nSeznam bodu zajmu byl ulozen do JSON souboru.")
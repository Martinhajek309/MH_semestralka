import copy
import json
from pathlib import Path


def vypis_body(nadpis, body):
    print(f"\n{nadpis}")
    for bod in body:
        print(
            f"- ID {bod['id']}: {bod['nazev']} | typ: {bod['typ']} | "
            f"hodnoceni: {bod.get('hodnoceni', 'Nezname')}"
        )


bod_zajmu = {
    "id": 1,
    "nazev": "Kavarna Na Rynku",
    "souradnice": (49.1951, 16.6068),
    "typ": "restaurace",
    "oteviraci_hodiny": {
        "po": "08:00-20:00",
        "ut": "08:00-20:00",
        "st": "08:00-20:00",
        "ct": "08:00-21:00",
        "pa": "08:00-22:00",
        "so": "09:00-22:00",
        "ne": "09:00-18:00",
    },
}

print("Vypis jednoho bodu zajmu pomoci .items():")
for klic, hodnota in bod_zajmu.items():
    print(f"{klic}: {hodnota}")


body_zajmu = [
    bod_zajmu,
    {
        "id": 2,
        "nazev": "Hrad Spilberk",
        "souradnice": (49.1949, 16.5990),
        "typ": "pamatka",
        "oteviraci_hodiny": {
            "po": "10:00-18:00",
            "ut": "10:00-18:00",
            "st": "10:00-18:00",
            "ct": "10:00-18:00",
            "pa": "10:00-18:00",
            "so": "09:00-19:00",
            "ne": "09:00-19:00",
        },
    },
    {
        "id": 3,
        "nazev": "Botanicka Zahrada",
        "souradnice": (49.2072, 16.6004),
        "typ": "park",
        "oteviraci_hodiny": {
            "po": "09:00-17:00",
            "ut": "09:00-17:00",
            "st": "09:00-17:00",
            "ct": "09:00-17:00",
            "pa": "09:00-17:00",
            "so": "09:00-17:00",
            "ne": "09:00-17:00",
        },
    },
    {
        "id": 4,
        "nazev": "Bistro U Mostu",
        "souradnice": (49.1988, 16.6111),
        "typ": "restaurace",
        "oteviraci_hodiny": {
            "po": "11:00-22:00",
            "ut": "11:00-22:00",
            "st": "11:00-22:00",
            "ct": "11:00-22:00",
            "pa": "11:00-23:00",
            "so": "11:00-23:00",
            "ne": "11:00-20:00",
        },
    },
]

hledany_typ = "restaurace"
print(f"\nBody zajmu typu '{hledany_typ}':")
for bod in body_zajmu:
    if bod["typ"] == hledany_typ:
        print(f"- {bod['nazev']} na souradnicich {bod['souradnice']}")


hodnoceni_pro_kazdy_druhy = [4.8, 3.7]
for poradi, index in enumerate(range(1, len(body_zajmu), 2)):
    body_zajmu[index]["hodnoceni"] = hodnoceni_pro_kazdy_druhy[poradi]

body_zajmu.sort(key=lambda bod: bod.get("hodnoceni", 0), reverse=True)
vypis_body("Body zajmu serazene podle hodnoceni:", body_zajmu)

print("\nBezpecny vypis atributu 'hodnoceni':")
for bod in body_zajmu:
    print(f"- {bod['nazev']}: {bod.get('hodnoceni', 'Nezname')}")


body_s_hodnocenim = {
    bod["id"]: bod
    for bod in body_zajmu
    if bod.get("hodnoceni", 0) > 3
}

print("\nSlovnik bodu s hodnocenim vyssim nez 3:")
for bod_id, bod in body_s_hodnocenim.items():
    print(f"{bod_id}: {bod['nazev']} -> {bod['hodnoceni']}")


puvodni_pro_kopie = copy.deepcopy(body_zajmu)
melka_kopie = puvodni_pro_kopie.copy()
hluboka_kopie = copy.deepcopy(puvodni_pro_kopie)

melka_kopie[0]["oteviraci_hodiny"]["po"] = "zavreno"
hluboka_kopie[0]["oteviraci_hodiny"]["ut"] = "12:00-18:00"

print("\nDemonstrace rozdilu mezi melkou a hlubokou kopii:")
print(f"Puvodni seznam - pondeli prvniho bodu: {puvodni_pro_kopie[0]['oteviraci_hodiny']['po']}")
print(f"Melka kopie - pondeli prvniho bodu: {melka_kopie[0]['oteviraci_hodiny']['po']}")
print(f"Puvodni seznam - utery prvniho bodu: {puvodni_pro_kopie[0]['oteviraci_hodiny']['ut']}")
print(f"Hluboka kopie - utery prvniho bodu: {hluboka_kopie[0]['oteviraci_hodiny']['ut']}")


json_cesta = Path(__file__).with_name("body_zajmu_svoboda.json")
with json_cesta.open("w", encoding="utf-8") as soubor:
    json.dump(body_zajmu, soubor, ensure_ascii=False, indent=4)

print(f"\nJSON soubor byl ulozen do: {json_cesta.name}")

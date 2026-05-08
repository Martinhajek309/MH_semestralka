bod1 = {
    "ID": 1,
    "nazev": "Restaurace Alfa",
    "souradnice": (10, 20),
    "typ": "restaurace",
    "oteviraci_hodiny": {
        "pondeli": "8-20",
        "utery": "8-20",
        "streda": "8-20",
        "ctvrtek": "8-20",
        "patek": "8-22",
        "sobota": "10-22",
        "nedele": "10-18"
    }
}

for klic, hodnota in bod1.items():
    print(f"{klic}: {hodnota}")

body = [
    bod1,
    {
        "ID": 2,
        "nazev": "Hrad",
        "souradnice": (15, 25),
        "typ": "pamatka",
        "oteviraci_hodiny": {"pondeli": "9-17"}
    },
    {
        "ID": 3,
        "nazev": "Restaurace Beta",
        "souradnice": (12, 22),
        "typ": "restaurace",
        "oteviraci_hodiny": {"pondeli": "10-22"}
    },
    {
        "ID": 4,
        "nazev": "Muzeum",
        "souradnice": (18, 30),
        "typ": "pamatka",
        "oteviraci_hodiny": {"pondeli": "zavreno"}
    }
]

print("\nRestaurace:")
for bod in body:
    if bod["typ"] == "restaurace":
        print(bod["nazev"])

body[1]["hodnoceni"] = 4.8
body[3]["hodnoceni"] = 4.2

body = sorted(body, key=lambda b: b.get("hodnoceni", 0), reverse=True)

print("\nSeřazeno podle hodnocení:")
for bod in body:
    print(bod["nazev"], "-", bod.get("hodnoceni", "Neznámé"))

import copy
import json

# Původní seznam bodů zájmu
body_zajmu = [
    {
        "ID": 1,
        "nazev": "Kavárna U Náměstí",
        "souradnice": (49.5938, 17.2509),
        "typ": "restaurace",
        "oteviraci_hodiny": {
            "pondeli": "8:00-20:00",
            "utery": "8:00-20:00"
        }
    },
    {
        "ID": 2,
        "nazev": "Hrad",
        "souradnice": (49.5950, 17.2515),
        "typ": "pamatka",
        "oteviraci_hodiny": {
            "pondeli": "9:00-17:00",
            "utery": "9:00-17:00"
        },
        "hodnoceni": 4.7
    },
    {
        "ID": 3,
        "nazev": "Pizzerie Napoli",
        "souradnice": (49.5942, 17.2520),
        "typ": "restaurace",
        "oteviraci_hodiny": {
            "pondeli": "11:00-22:00",
            "utery": "11:00-22:00"
        },
        "hodnoceni": 3.5
    },
    {
        "ID": 4,
        "nazev": "Městské muzeum",
        "souradnice": (49.5960, 17.2530),
        "typ": "pamatka",
        "oteviraci_hodiny": {
            "pondeli": "zavreno",
            "utery": "9:00-16:00"
        },
        "hodnoceni": 2.8
    }
]

# 1. Převod seznamu na slovník pomocí dictionary comprehension
# zahrnuty budou jen body s hodnocením vyšším než 3
slovnik_bodu = {
    bod["ID"]: bod
    for bod in body_zajmu
    if bod.get("hodnoceni", 0) > 3
}

print("1. Slovník bodů zájmu s hodnocením > 3:")
for klic, hodnota in slovnik_bodu.items():
    print(f"{klic}: {hodnota}")

print("-" * 50)

# 2. Mělká a hluboká kopie seznamu
mělka_kopie = copy.copy(body_zajmu)
hluboka_kopie = copy.deepcopy(body_zajmu)

# Změníme vnořený atribut v mělké kopii
mělka_kopie[0]["oteviraci_hodiny"]["pondeli"] = "ZMENENO_V_MELKE_KOPII"

# Změníme vnořený atribut v hluboké kopii
hluboka_kopie[1]["oteviraci_hodiny"]["pondeli"] = "ZMENENO_V_HLUBOKE_KOPII"

print("2. Demonstrace rozdílu mezi mělkou a hlubokou kopií:\n")

print("Původní seznam:")
print(body_zajmu[0]["nazev"], "-", body_zajmu[0]["oteviraci_hodiny"]["pondeli"])
print(body_zajmu[1]["nazev"], "-", body_zajmu[1]["oteviraci_hodiny"]["pondeli"])

print("\nMělká kopie:")
print(mělka_kopie[0]["nazev"], "-", mělka_kopie[0]["oteviraci_hodiny"]["pondeli"])
print(mělka_kopie[1]["nazev"], "-", mělka_kopie[1]["oteviraci_hodiny"]["pondeli"])

print("\nHluboká kopie:")
print(hluboka_kopie[0]["nazev"], "-", hluboka_kopie[0]["oteviraci_hodiny"]["pondeli"])
print(hluboka_kopie[1]["nazev"], "-", hluboka_kopie[1]["oteviraci_hodiny"]["pondeli"])

print("\nVysvětlení:")
print("Změna v mělké kopii se projevila i v původním seznamu, protože vnořené objekty jsou sdílené.")
print("Změna v hluboké kopii se v původním seznamu neprojevila, protože deepcopy vytvoří úplně nezávislou kopii.")

print("-" * 50)

# 3. Serializace do JSON souboru
# nahraďte VASEPRIJMENI svým skutečným příjmením
nazev_souboru = "body_zajmu_VASEPRIJMENI.json"

with open(nazev_souboru, "w", encoding="utf-8") as soubor:
    json.dump(body_zajmu, soubor, ensure_ascii=False, indent=4)

print(f"3. Data byla uložena do souboru: {nazev_souboru}")
import json
from copy import copy, deepcopy

# ÚKOL 1: Slovníky (Blok L8-1)

# 1. Vytvoření slovníku reprezentujícího bod zájmu
bod_zajmu = {
    "ID": 1,
    "název": "Restaurace U Zlatého Lva",
    "souřadnice": {"x": 50.5928, "y": 15.4730},
    "typ": "restaurace",
    "otevírací_hodiny": {
        "pondělí": "10:00-22:00",
        "úterý": "10:00-22:00",
        "středa": "10:00-22:00",
        "čtvrtek": "10:00-22:00",
        "pátek": "10:00-23:00",
        "sobota": "11:00-23:00",
        "neděle": "11:00-21:00"
    }
}

# 2. Výpis všech klíčů a hodnot slovníku
print("=" * 50)
print("VÝPIS SLOVNÍKU - Formát: klíč: hodnota")
print("=" * 50)
for klic, hodnota in bod_zajmu.items():
    print(f"{klic}: {hodnota}")

# 3. Seznam obsahující alespoň 3 body zájmu
body_zajmu = [
    {
        "ID": 1,
        "název": "Restaurace U Zlatého Lva",
        "souřadnice": {"x": 50.5928, "y": 15.4730},
        "typ": "restaurace",
        "otevírací_hodiny": {
            "pondělí": "10:00-22:00",
            "sobota": "11:00-23:00"
        }
    },
    {
        "ID": 2,
        "název": "Svatý Kopeček",
        "souřadnice": {"x": 50.5916, "y": 15.4756},
        "typ": "památka",
        "otevírací_hodiny": {
            "pondělí": "09:00-17:00",
            "sobota": "09:00-17:00"
        }
    },
    {
        "ID": 3,
        "název": "Pizzerie Napoli",
        "souřadnice": {"x": 50.5940, "y": 15.4720},
        "typ": "restaurace",
        "otevírací_hodiny": {
            "pondělí": "11:00-23:00",
            "sobota": "12:00-23:00"
        }
    },
    {
        "ID": 4,
        "název": "Múzeum umění",
        "souřadnice": {"x": 50.5950, "y": 15.4710},
        "typ": "památka",
        "otevírací_hodiny": {
            "pondělí": "10:00-18:00",
            "sobota": "10:00-20:00"
        }
    }
]

# Vyhledání a výpis bodů určitého typu (např. restaurace)
print("\n" + "=" * 50)
print("HLEDÁNÍ BODŮ PODLE TYPU - Restaurace")
print("=" * 50)
typ_hledany = "restaurace"
for bod in body_zajmu:
    if bod["typ"] == typ_hledany:
        print(f"ID: {bod['ID']}, Název: {bod['název']}, Typ: {bod['typ']}")

# 4. Rozšíření každého druhého bodu o atribut "hodnoceni"
print("\n" + "=" * 50)
print("PŘIDÁNÍ HODNOCENÍ KE KAŽDÉMU DRUHÉMU BODU")
print("=" * 50)
body_zajmu[0]["hodnoceni"] = 4.5
body_zajmu[2]["hodnoceni"] = 4.8

# Seřazení podle hodnocení
body_zajmu_serazene = sorted(
    [bod for bod in body_zajmu if "hodnoceni" in bod],
    key=lambda bod: bod["hodnoceni"],
    reverse=True
)

print("Body seřazené podle hodnocení (sestupně):")
for bod in body_zajmu_serazene:
    print(f"  {bod['název']}: {bod['hodnoceni']} ⭐")

# 5. Bezpečný výpis atributu s výchozí hodnotou ".get()"
print("\n" + "=" * 50)
print("BEZPEČNÝ VÝPIS ATRIBUTU S VÝCHOZÍ HODNOTOU")
print("=" * 50)
for bod in body_zajmu:
    hodnoceni = bod.get("hodnoceni", "Neznámé")
    print(f"{bod['název']}: Hodnocení = {hodnoceni}")

# ÚKOL 2: Pokročilé metody slovníků (Blok L8-2)

# 1. Převod seznamu na slovník pomocí dictionary comprehension
print("\n" + "=" * 50)
print("DICTIONARY COMPREHENSION - Body s hodnocením > 3")
print("=" * 50)

slovnik_body_zajmu = {
    bod["ID"]: bod 
    for bod in body_zajmu 
    if bod.get("hodnoceni", 0) > 3
}

print("Vytvořený slovník:")
for id_bodu, atributy in slovnik_body_zajmu.items():
    print(f"  ID {id_bodu}: {atributy['název']} (Hodnocení: {atributy.get('hodnoceni', 'N/A')})")

# 2. Mělká a hluboká kopie
print("\n" + "=" * 50)
print("MĚLKÁ A HLUBOKÁ KOPIE - Difference")
print("=" * 50)

# Vytvoření mělké a hluboké kopie
body_zajmu_melka = copy(body_zajmu)
body_zajmu_hluboka = deepcopy(body_zajmu)

# Změna vnořeného atributu (souřadnice) v původním seznamu
print("Původní souřadnice bodu 1: x =", body_zajmu[0]["souřadnice"]["x"])

body_zajmu[0]["souřadnice"]["x"] = 99.9999

print(f"\nPo změně na {body_zajmu[0]['souřadnice']['x']}:")
print(f"  Původní seznam: x = {body_zajmu[0]['souřadnice']['x']}")
print(f"  Mělká kopie: x = {body_zajmu_melka[0]['souřadnice']['x']} ⚠️ (změna se projevila!)")
print(f"  Hluboká kopie: x = {body_zajmu_hluboka[0]['souřadnice']['x']} ✓ (změna se neprojevila)")

# Návrat na původní hodnotu
body_zajmu[0]["souřadnice"]["x"] = 50.5928

# 3. Serializace do JSON souboru
print("\n" + "=" * 50)
print("SERIALIZACE DO JSON SOUBORU")
print("=" * 50)

json_filename = "body_zajmu_cip.json"

with open(json_filename, "w", encoding="utf-8") as json_file:
    json.dump(body_zajmu, json_file, ensure_ascii=False, indent=2)

print(f"✓ Soubor '{json_filename}' byl úspěšně vytvořen!")
print(f"  Cesta: c:\\Users\\danie\\OneDrive - Univerzita Palackého v Olomouci\\Plocha\\school\\summer semester\\PRODA\\visual_studio_code\\KGI-PRODA-2026\\cviceni7\\cip\\{json_filename}")
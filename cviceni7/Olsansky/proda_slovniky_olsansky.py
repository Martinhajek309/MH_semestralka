import copy
import json

# ==========================================
# Úkol 1: Slovníky (Blok L8-1)
# ==========================================

print("--- Úkol 1.1 a 1.2 ---")
# 1. Slovník reprezentující bod zájmu
bod_zajmu = {
    "ID": 1,
    "nazev_bodu": "U Dřeváka",
    "souradnice": (49.206, 16.602),
    "typ": "restaurace",
    "oteviraci_hodiny": {
        "po": "11:00-23:00",
        "ut": "11:00-23:00",
        "st": "11:00-23:00",
        "ct": "11:00-23:00",
        "pa": "11:00-01:00",
        "so": "11:00-01:00",
        "ne": "11:00-22:00"
    }
}

# 2. Výpis všech klíčů a hodnot
for klic, hodnota in bod_zajmu.items():
    print(f"{klic}: {hodnota}")

print("\n--- Úkol 1.3 ---")
# 3. Seznam bodů zájmu
body_zajmu = [
    bod_zajmu,
    {
        "ID": 2,
        "nazev_bodu": "Hrad Špilberk",
        "souradnice": (49.194, 16.599),
        "typ": "památka",
        "oteviraci_hodiny": {
            "po": "Zavřeno",
            "ut": "09:00-17:00",
            "st": "09:00-17:00",
            "ct": "09:00-17:00",
            "pa": "09:00-17:00",
            "so": "09:00-17:00",
            "ne": "09:00-17:00"
        }
    },
    {
        "ID": 3,
        "nazev_bodu": "Stopkova Plzeňská Pivnice",
        "souradnice": (49.196, 16.606),
        "typ": "restaurace",
        "oteviraci_hodiny": {
            "po": "11:00-24:00",
            "ut": "11:00-24:00",
            "st": "11:00-24:00",
            "ct": "11:00-24:00",
            "pa": "11:00-24:00",
            "so": "11:00-24:00",
            "ne": "11:00-23:00"
        }
    },
    {
        "ID": 4,
        "nazev_bodu": "Katedrála sv. Petra a Pavla",
        "souradnice": (49.191, 16.607),
        "typ": "památka",
        "oteviraci_hodiny": {
            "po": "08:15-18:30",
            "ut": "08:15-18:30",
            "st": "08:15-18:30",
            "ct": "08:15-18:30",
            "pa": "08:15-18:30",
            "so": "08:15-18:30",
            "ne": "08:15-18:30"
        }
    }
]

# Vyhledání a výpis bodů určitého typu (restaurace)
print("Vyhledané restaurace:")
for bod in body_zajmu:
    if bod["typ"] == "restaurace":
        print("-", bod["nazev_bodu"])

print("\n--- Úkol 1.4 ---")
# 4. Rozšíření každého druhého bodu zájmu o atribut "hodnoceni" a seřazení
hodnoceni_k_prirazeni = [4.5, 3.8] # pomocný seznam hodnocení
index_hodnoceni = 0

for i in range(1, len(body_zajmu), 2):
    body_zajmu[i]["hodnoceni"] = hodnoceni_k_prirazeni[index_hodnoceni]
    index_hodnoceni += 1

# Seřazení podle hodnocení (seznam může obsahovat body bez hodnocení, použijeme .get() s defaultní hodnotou 0)
body_zajmu.sort(key=lambda x: x.get("hodnoceni", 0), reverse=True)

for bod in body_zajmu:
    print(f"{bod['nazev_bodu']} (ID: {bod['ID']})")

print("\n--- Úkol 1.5 ---")
# 5. Bezpečný výpis atributu, který nemusí existovat
for bod in body_zajmu:
    hodnoceni = bod.get("hodnoceni", "Neznámé")
    print(f"Bod: {bod['nazev_bodu']:<30} Hodnocení: {hodnoceni}")


# ==========================================
# Úkol 2: Pokročilé metody slovníků (Blok L8-2)
# ==========================================

print("\n--- Úkol 2.1 ---")
# 1. Převod seznamu na slovník pomocí dictionary comprehension + filtrace (hodnoceni > 3)
lepsi_body_dict = {bod["ID"]: bod for bod in body_zajmu if bod.get("hodnoceni", 0) > 3}
print("Body zájmu převedené na slovník (s hodnocením nad 3):")
for klic, hodnota in lepsi_body_dict.items():
    print(f"ID {klic}: {hodnota['nazev_bodu']}")

print("\n--- Úkol 2.2 ---")
# 2. Mělká a hluboká kopie
melka_kopie = copy.copy(body_zajmu)
hluboka_kopie = copy.deepcopy(body_zajmu)

# Změna vnořeného atributu (otevírací doba v pondělí u jedné ukázky) v původním seznamu
# U mělkých kopií se zkopíruje jen reference na vnitřní objekty (slovník oteviraci_hodiny), 
# takže změna se projeví v původním seznamu i v mělké kopii.
# V hluboké kopii se vytvořila zcela nezávislá kopie všech vnořených objektů.
if body_zajmu:
    prvni_bod = body_zajmu[0]
    # Uložíme si původní pro kontrolu a změníme
    prvni_bod["oteviraci_hodiny"]["po"] = "ZAVŘENO - sanitární den"
    
    print(f"Původní seznam: {body_zajmu[0]['oteviraci_hodiny']['po']}")
    print(f"Mělká kopie :   {melka_kopie[0]['oteviraci_hodiny']['po']}")
    print(f"Hluboká kopie:  {hluboka_kopie[0]['oteviraci_hodiny']['po']}")

print("\n--- Úkol 2.3 ---")
# 3. Serializace seznamu do JSON
json_soubor = "/home/ayabp/KGI-PRODA-2026/cviceni7/Olsansky/body_zajmu_Olsansky.json"
with open(json_soubor, "w", encoding="utf-8") as f:
    json.dump(body_zajmu, f, ensure_ascii=False, indent=4)
print(f"Data byla serializována a uložena do souboru {json_soubor}.")

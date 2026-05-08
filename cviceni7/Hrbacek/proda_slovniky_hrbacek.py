import json
import copy

# =========================
# ÚKOL 1
# =========================

# 1. Slovník bodu zájmu
bod1 = {
    "id": 1,
    "nazev": "Restaurace U Tří Lip",
    "souradnice": (49.5938, 17.2509),
    "typ": "restaurace",
    "oteviraci_hodiny": {
        "po": "11-22",
        "ut": "11-22",
        "st": "11-22",
        "ct": "11-22",
        "pa": "11-23",
        "so": "12-23",
        "ne": "12-20"
    }
}

# 2. Výpis klíčů a hodnot
print("=== Výpis bodu 1 ===")
for klic, hodnota in bod1.items():
    print(f"{klic}: {hodnota}")

# 3. Seznam bodů zájmu
body = [
    bod1,
    {
        "id": 2,
        "nazev": "Katedrála sv. Václava",
        "souradnice": (49.5952, 17.2611),
        "typ": "pamatka",
        "oteviraci_hodiny": {"po": "9-17"}
    },
    {
        "id": 3,
        "nazev": "Café 87",
        "souradnice": (49.5930, 17.2515),
        "typ": "restaurace",
        "oteviraci_hodiny": {"po": "8-20"}
    }
]

print("\n=== Restaurace ===")
for bod in body:
    if bod["typ"] == "restaurace":
        print(bod["nazev"])

# 4. Přidání hodnocení každému druhému bodu (index 1, 3, ...)
for i in range(len(body)):
    if i % 2 == 1:
        body[i]["hodnoceni"] = 4.5  # příklad

# Seřazení podle hodnocení (neexistující = 0)
body_serazene = sorted(body, key=lambda x: x.get("hodnoceni", 0), reverse=True)

print("\n=== Seřazené body ===")
for bod in body_serazene:
    print(bod["nazev"], "-", bod.get("hodnoceni", "Neznámé"))

# 5. Bezpečný výpis atributu
print("\n=== Bezpečný výpis hodnocení ===")
for bod in body:
    print(bod["nazev"], "->", bod.get("hodnoceni", "Neznámé"))



# 1. Dictionary comprehension (jen hodnocení > 3)
body_dict = {
    bod["id"]: bod
    for bod in body
    if bod.get("hodnoceni", 0) > 3
}

print("\n=== Dictionary podle ID ===")
for k, v in body_dict.items():
    print(k, ":", v["nazev"])

# 2. Mělká vs hluboká kopie
melka_kopie = body.copy()
hluboka_kopie = copy.deepcopy(body)

# změna vnořeného atributu
melka_kopie[0]["nazev"] = "ZMĚNA MĚLKÁ"
hluboka_kopie[1]["nazev"] = "ZMĚNA HLUBOKÁ"

print("\n=== Porovnání kopií ===")
print("Originál:", body[0]["nazev"])  # změněno!
print("Mělká:", melka_kopie[0]["nazev"])
print("Hluboká:", hluboka_kopie[1]["nazev"])
print("Originál (hluboká):", body[1]["nazev"])  # nezměněno

# 3. Serializace do JSON
with open("cviceni7/Hrbacek/body_zajmu_hrbacek.json", "w", encoding="utf-8") as f:
    json.dump(body, f, ensure_ascii=False, indent=4)

print("\nJSON soubor byl uložen.")
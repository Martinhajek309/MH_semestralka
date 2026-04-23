bod = {
    "ID": 1,
    "nazev": "Restaurace Na Rynku",
    "souradnice": (49.5938, 17.2509),
    "typ": "restaurace",
    "oteviraci_hodiny": {
        "po": "11:00-22:00",
        "ut": "11:00-22:00",
        "st": "11:00-22:00",
        "ct": "11:00-22:00",
        "pa": "11:00-23:00",
        "so": "12:00-23:00",
        "ne": "12:00-21:00"
    }
}

print("=== Výpis slovníku ===")
for klic, hodnota in bod.items():
    print(f"{klic}: {hodnota}")

body = [
    {
        "ID": 1,
        "nazev": "Restaurace Na Rynku",
        "souradnice": (49.5938, 17.2509),
        "typ": "restaurace"
    },
    {
        "ID": 2,
        "nazev": "Orloj v Olomouci",
        "souradnice": (49.5950, 17.2512),
        "typ": "pamatka"
    },
    {
        "ID": 3,
        "nazev": "Café New One",
        "souradnice": (49.5945, 17.2520),
        "typ": "restaurace"
    }
]

print("\n=== Restaurace ===")
for b in body:
    if b["typ"] == "restaurace":
        print(b["nazev"])

for i in range(1, len(body), 2):
    body[i]["hodnoceni"] = 4.5 + i

body_sorted = sorted(body, key=lambda x: x.get("hodnoceni", 0), reverse=True)

print("\n=== Seřazené body podle hodnocení ===")
for b in body_sorted:
    print(b)

print("\n=== Hodnocení ===")
for b in body:
    print(f"{b['nazev']} - hodnocení: {b.get('hodnoceni', 'Neznámé')}")

# část 2

body_dict = {
    b["ID"]: b
    for b in body
    if b.get("hodnoceni", 0) > 3
}

print("\n=== Slovník (jen hodnocení > 3) ===")
print(body_dict)


import copy

shallow_copy = body.copy()
deep_copy = copy.deepcopy(body)

body[1]["nazev"] = "ZMĚNĚNO - Orloj"

print("\n=== Mělká kopie ===")
print(shallow_copy)

print("\n=== Hluboká kopie ===")
print(deep_copy)

# vysvětlení:
print("\n=== Vysvětlení ===")
print("Mělká kopie se změnila:", shallow_copy[1]["nazev"])
print("Hluboká kopie zůstala původní:", deep_copy[1]["nazev"])

import json

with open("body_zajmu_Tobola.json", "w", encoding="utf-8") as f:
    json.dump(body, f, ensure_ascii=False, indent=4)

print("\nJSON soubor byl vytvořen.")
from __future__ import annotations
import copy
import json
from pathlib import Path

def vytvor_bod_zajmu() -> dict:
    return {
        "id": 1,
        "nazev": "Café Central",
        "souřadnice": (14.42076, 50.08804),
        "typ": "restaurace",
        "oteviraci_hodiny": {
            "pondeli": "8:00-20:00",
            "utery": "8:00-20:00",
            "streda": "8:00-20:00",
            "ctvrtek": "8:00-20:00",
            "patek": "8:00-22:00",
            "sobota": "9:00-22:00",
            "nedele": "9:00-18:00",
        },
    }


def vypis_slovnik(slovnik: dict) -> None:
    for klic, hodnota in slovnik.items():
        print(f"{klic}: {hodnota}")


def main() -> None:
    bod = vytvor_bod_zajmu()

    print("=== Úkol 1.1 a 1.2 ===")
    vypis_slovnik(bod)
    print()

    body_zajmu = [
        {
            "id": 1,
            "nazev": "Café Central",
            "souřadnice": (14.42076, 50.08804),
            "typ": "restaurace",
            "oteviraci_hodiny": {
                "pondeli": "8:00-20:00",
                "utery": "8:00-20:00",
                "streda": "8:00-20:00",
                "ctvrtek": "8:00-20:00",
                "patek": "8:00-22:00",
                "sobota": "9:00-22:00",
                "nedele": "9:00-18:00",
            },
        },
        {
            "id": 2,
            "nazev": "Karlův most",
            "souřadnice": (14.41144, 50.08650),
            "typ": "památka",
            "oteviraci_hodiny": {
                "pondeli": "nonstop",
                "utery": "nonstop",
                "streda": "nonstop",
                "ctvrtek": "nonstop",
                "patek": "nonstop",
                "sobota": "nonstop",
                "nedele": "nonstop",
            },
        },
        {
            "id": 3,
            "nazev": "Bistro U Tří",
            "souřadnice": (14.42500, 50.09000),
            "typ": "restaurace",
            "oteviraci_hodiny": {
                "pondeli": "10:00-18:00",
                "utery": "10:00-18:00",
                "streda": "10:00-18:00",
                "ctvrtek": "10:00-18:00",
                "patek": "10:00-20:00",
                "sobota": "11:00-20:00",
                "nedele": "zavřeno",
            },
        },
    ]

    print("=== Úkol 1.3 ===")
    hledany_typ = "restaurace"
    for bod_zajmu in body_zajmu:
        if bod_zajmu["typ"] == hledany_typ:
            print(f"Najdeno: {bod_zajmu['nazev']} ({bod_zajmu['typ']})")
    print()

    print("=== Úkol 1.4 ===")
    for i in range(0, len(body_zajmu), 2):
        body_zajmu[i]["hodnoceni"] = 4.5 - i * 0.3

    body_zajmu.sort(key=lambda bod_zajmu: bod_zajmu.get("hodnoceni", 0), reverse=True)
    for bod_zajmu in body_zajmu:
        print(
            f"{bod_zajmu['nazev']}: hodnoceni={bod_zajmu.get('hodnoceni', 'není uvedeno')}"
        )
    print()

    print("=== Úkol 1.5 ===")
    for bod_zajmu in body_zajmu:
        print(f"{bod_zajmu['nazev']}: {bod_zajmu.get('popis', 'Neznámé')}")
    print()

    print("=== Úkol 2.1 ===")
    body_zajmu_vybrane = {
        bod_zajmu["id"]: bod_zajmu
        for bod_zajmu in body_zajmu
        if bod_zajmu.get("hodnoceni", 0) > 3
    }
    for klic, hodnota in body_zajmu_vybrane.items():
        print(f"{klic}: {hodnota['nazev']} ({hodnota.get('hodnoceni')})")
    print()

    print("=== Úkol 2.2 ===")
    shallow_kopie = copy.copy(body_zajmu)
    deep_kopie = copy.deepcopy(body_zajmu)

    body_zajmu[0]["oteviraci_hodiny"]["pondeli"] = "9:00-21:00"

    print("Původní seznam:")
    print(body_zajmu[0]["oteviraci_hodiny"]["pondeli"])
    print("Mělká kopie:")
    print(shallow_kopie[0]["oteviraci_hodiny"]["pondeli"])
    print("Hluboká kopie:")
    print(deep_kopie[0]["oteviraci_hodiny"]["pondeli"])
    print()

    print("=== Úkol 2.3 ===")
    vystupni_soubor = Path(__file__).with_name("body_zajmu_Mikeska.json")
    with vystupni_soubor.open("w", encoding="utf-8") as soubor:
        json.dump(body_zajmu, soubor, ensure_ascii=False, indent=2)
    print(f"Uloženo do: {vystupni_soubor}")


if __name__ == "__main__":
    main()
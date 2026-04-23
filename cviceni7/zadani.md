# L8: Praktická cvičení — Slovníky (Dictionaries)

## Git Workflow (před začátkem)

1. **Pullněte** si nejnovější verzi repozitáře.
2. Vytvořte si novou větev ve formátu `cviceni7/prijmeni`.
3. Všechny úkoly vypracujte do složky `cviceni7/prijmeni`.

---

## Úkol 1: Slovníky (Blok L8-1)

_Vytvořte skript `proda_slovniky_prijmeni.py`_

1. Vytvořte slovník reprezentující **bod zájmu** s klíči: ID, název bodu, souřadnice `(x, y)`, typ (např. `"restaurace"`, `"památka"`), a otevírací hodiny v jednotlivých dnech v týdnu.
2. Napište kód, který vypíše všechny klíče a hodnoty slovníku formátované jako _"klíč: hodnota"_ (využijte `.items()`).
3. Vytvořte **seznam** obsahující alespoň 3 body zájmu a napište cyklus, který vyhledá a vypíše všechny body určitého typu (např. všechny `"restaurace"`).
4. Rozšiřte **každý druhý** bod zájmu o nový atribut `"hodnoceni"` pomocí indexace a poté celý seznam seřaďte podle hodnocení.
5. Bezpečně vypište atribut, který nemusí existovat u všech bodů, s výchozí hodnotou `"Neznámé"` (využijte `.get()`).

---

## Úkol 2: Pokročilé metody slovníků (Blok L8-2)

_Pokračujte v souboru `proda_slovniky_prijmeni.py`_

1. Převeďte seznam bodů zájmu na slovník pomocí **dictionary comprehension** tak, aby:
   - klíčem bylo ID bodu
   - hodnotou byl celý slovník s atributy
   - zahrnuty byly pouze body s hodnocením vyšším než 3
2. Vytvořte **mělkou** a **hlubokou** kopii vašeho seznamu bodů zájmu a demonstrujte rozdíl mezi oběma přístupy (změňte vnořený atribut a ukažte, kde se změna projeví).
3. Serializujte seznam bodů zájmu do JSON souboru `body_zajmu_VASEPRIJMENI.json` (nezapomeňte na `ensure_ascii=False`).

---

## Odevzdání

1. Uložte soubor `proda_slovniky_prijmeni.py`.
2. Proveďte **Stage**, **Commit** (srozumitelná zpráva) a **Push** do své větve.
3. Vytvořte na GitHubu **Pull Request** do hlavní větve.

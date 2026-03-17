# L6: Praktická cvičení — Seznamy (Lists)

## Git Workflow (před začátkem)

1. **Pullněte** si nejnovější verzi repozitáře.
2. Vytvořte si novou větev ve formátu `cviceni5/prijmeni`.
3. Všechny úkoly vypracujte do složky `cviceni5/prijmeni`.

---

## Úkol 1: Definice seznamů a výběr prvků (Blok L6-1)

_Vytvořte skript `listy_prijmeni.py`_

1. Vytvořte seznam souřadnic `[lon, lat]` reprezentující polygon — **pětiúhelník** (5 vrcholů + opakovaný první bod pro uzavření).
2. Vytvořte **multi-polygon** — seznam obsahující váš pětiúhelník a druhý polygon (čtverec).
3. Použijte **indexování** k získání druhého vrcholu prvního polygonu.
4. Použijte **slicing** k získání posledních tří vrcholů druhého polygonu, seřazených **pozpátku**.
5. Všechny výsledky vypište pomocí `print()` a okomentujte.

---

## Úkol 2: Metody a funkce (Blok L6-2)

_Pokračujte v souboru `listy_prijmeni.py`_

1. Vytvořte seznam bodů (jako souřadnice `[lon, lat]`) reprezentující **trasu** (alespoň 4 body).
2. Přidejte do trasy nový bod na konec pomocí `append`.
3. Vložte bod **doprostřed** trasy pomocí `insert`.
4. Pomocí `sorted()` vytvořte nový seznam bodů seřazených podle lat (y-souřadnice).
5. Spočítejte **průměrnou** lon a lat souřadnici všech bodů v trase (využijte `sum()` a `len()`).

---

## Úkol 3: Pokročilé procházení a list comprehension (Blok L6-3)

_Pokračujte v souboru `listy_prijmeni.py`_

1. Vytvořte seznam souřadnic `[lon, lat, výška]` — alespoň **5 bodů** reprezentujících výškový profil trasy.
2. Pomocí `enumerate` projděte body a vypište: _"Bod {číslo}: výška {výška} m n. m."_
3. Vypočítejte **průměrnou** nadmořskou výšku trasy.
4. Pomocí **list comprehension** vytvořte:
   - Seznam bodů s výškou **větší než průměr**
   - Seznam obsahující **pouze výšky** (bez souřadnic)
5. Výsledky vypište s komentáři.

---

## Odevzdání

1. Uložte soubor `listy_prijmeni.py`.
2. Proveďte **Stage**, **Commit** (srozumitelná zpráva) a **Push** do své větve.
3. Vytvořte na GitHubu **Pull Request** do hlavní větve.

> [!tip] Tip
> Pokud si nevíte rady se syntaxí, podívejte se do materiálů k jednotlivým blokům (L6-1, L6-2, L6-3). Nezapomínejte na komentáře vysvětlující, co daný kód dělá!

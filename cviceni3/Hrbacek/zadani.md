# L4: Praktická cvičení — Základy Pythonu

## Git Workflow (před začátkem)

1. **Pullněte** si nejnovější verzi repozitáře.
2. Vytvořte si novou větev ve formátu `cviceni4/prijmeni`.
3. Všechny úkoly vypracujte do složky `cviceni4/prijmeni`.

---

## Úkol 1: Proměnné a datové typy (Blok L4-1)

_Vytvořte skript `proda_1_mesto_prijmeni.py`_

1. **Definujte proměnné** pro vaše oblíbené město:
   - Název města (`str`)
   - Souřadnice (jako `list` dvou čísel: šířka a délka)
   - Počet obyvatel (`int`)
   - Rozloha v km² (`float`)
   - Informace, zda je hlavním městem (`bool`)
2. **Výpočty a výstupy**:
   - Vypočítejte hustotu zalidnění (obyvatel na km²).
   - Pomocí funkce `type()` vypište do terminálu typy všech vytvořených proměnných.
   - Pomocí `input()` se zeptejte uživatele na jeho jméno.
   - Vypište pomocí **f-stringu** větu ve formátu:  
     _"Ahoj [jméno], město [město] má hustotu [hustota] obyv./km² a nachází se na souřadnicích [souřadnice]."_

---

## Úkol 2: Podmínky a logika (Blok L4-2)

_Vytvořte skript `proda_2_podminky_prijmeni.py`_

Vytvořte program, který na základě vstupu od uživatele klasifikuje počasí:

1. **Vstupy**: Pomocí `input()` načtěte od uživatele aktuální **teplotu** a **vlhkost** (nezapomeňte na převod z textu na číslo).
2. **Podmínky**:
   - Pokud je teplota pod 0°C, vypište: _"Mrzne"_.
   - Mezi 0 a 10°C (včetně): _"Je zima"_.
   - Mezi 10 a 25°C: _"Je mírné počasí"_.
   - Nad 25°C: _"Je teplo"_.
3. **Logické operátory**:
   - Pokud je teplota nad 25°C **a zároveň** vlhkost nad 70 %, vypište: _"Pozor na tropické vedro!"_
4. **Ošetření chyb**:
   - Pokud uživatel zadá vlhkost menší než 0 nebo větší než 100, vypište: _"Chyba: Neplatná hodnota vlhkosti!"_

---

## Úkol 3: Cykly a iterace (Blok L4-3)

_Vytvořte skript `proda_3_cykly_prijmeni.py`_

Představte si měření z meteostanice za 24 hodin (seznam 24 čísel). Senzor občas chybuje.

1. **Data**: Vytvořte seznam `mereni = [12.5, 13.2, 55.0, 14.1, -25.0, ...]` (doplňte alespoň 12 hodnot, vložte tam chyby: nad 50 a pod -20).
2. **Cyklus**: Pomocí `for` cyklu a funkce `enumerate()` projděte měření.
3. **Logika cyklu**:
   - Pomocí **indexu** z `enumerate` určete hodinu měření (index 0 = 0:00).
   - Pokud je teplota **nad 50°C**, vypište: _"Hodina [X]:00: Nesmyslná hodnota (káva na senzoru), přeskakuji."_ a použijte `continue`.
   - Pokud je teplota **pod -20°C**, vypište: _"Hodina [X]:00: Kritická chyba senzoru, ukončuji kontrolu!"_ a použijte `break`.
   - Pokud je teplota v pořádku, vypište: _"Teplota v [X]:00 byla [hodnota]°C."_
4. **Shrnutí**: Na konci programu vypište, kolik platných měření bylo úspěšně zpracováno.

---

## Odevzdání

1. Uložte všechny skripty.
2. Proveďte **Stage**, **Commit** (srozumitelná zpráva) a **Push** do své větve.
3. Vytvořte na GitHubu **Pull Request** do hlavní větve.

> [!tip] Tip
> Pokud si nevíte rady se syntaxí, podívejte se do materiálů k jednotlivým blokům (L4-1, L4-2, L4-3). Nezapomínejte na správné **odsazení kódu!**

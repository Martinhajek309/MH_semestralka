# L5: Praktická cvičení — Funkce v Pythonu

## Git Workflow (před začátkem)

1. Pullněte si nejnovější verzi repozitáře.
2. Vytvořte si novou větev ve formátu cviceni4/prijmeni.
3. Všechny úkoly vypracujte do složky cviceni4/prijmeni.

---

## Úkol 1: Základy funkcí (Blok L5-1)

_Vytvořte skript `geodistance_prijmeni.py`_

1. Vytvořte funkci `vypocitej_vzdalenost_od_rovniku`, která:
   - Přijímá jeden parametr sirka (zeměpisná šířka ve stupních)
   - Vypočítá vzdálenost od rovníku v kilometrech (1° ≈ 111,32 km)
   - Vyprintuje vypočtenou hodnotu
2. Vytvořte seznam zeměpisných šířek pro několik měst (např. 0, 15, 30, 45, 60).
3. Použijte for cyklus k výpočtu vzdálenosti pro každou šířku.
4. Výsledky vypište pomocí f-stringu ve formátu:
   _"Město na šířce {sirka}° je {vzdalenost} km od rovníku."_

---

## Úkol 2: Parametry, return a type hints (Blok L5-2)

_Pokračujte v souboru `geodistance_prijmeni.py`_

1. Rozšiřte funkci `vypocitej_vzdalenost_od_rovniku` tak, aby přijímala:
   - sirka (povinný) — zeměpisná šířka ve stupních
   - jednotka (volitelný) — výchozí hodnota "km", určuje jednotku vzdálenosti (kilometry nebo míle)
   - zaokrouhlit (volitelný) — výchozí hodnota False, určuje, zda zaokrouhlit na celé číslo
2. Upravte funkci tak, aby:
   - Vypočítala vzdálenost v zadané jednotce (1 km ≈ 0,621371 míle)
   - Zaokrouhlila výsledek, pokud je zaokrouhlit nastaveno na True
   - Vracela výsledek pomocí return (místo pouhého printu)
3. Použijte for cyklus k výpočtu vzdálenosti pro různé šířky a kombinace parametrů.
4. Výsledky vypište ve formátu: _"Město na šířce {sirka}° je {vzdalenost} {jednotka} od rovníku."_
5. Přidejte k funkci type hints pro všechny parametry a návratovou hodnotu.

---

## Úkol 3: Dokumentace a kvalita kódu (Blok L5-3)

_Pokračujte v souboru `geodistance_prijmeni.py`_

### Část A: Psaní a dokumentace

1. Přidejte k funkci `vypocitej_vzdalenost_od_rovniku` docstring, který popisuje účel funkce, parametry a návratovou hodnotu.
2. Vytvořte novou funkci vytvor_geojson_bod s parametry:
   - nazev (povinný) — název bodu
   - lat (povinný) — zeměpisná šířka
   - lon (povinný) — zeměpisná délka
3. Funkce vrátí textový řetězec obsahující validní GeoJSON bod s atributem nazev a vzdalenost_od_rovniku.
4. Přidejte type hints a docstring.
5. Zavolejte funkci pro existující místo, uložte výsledný GeoJSON do souboru misto_prijmeni.geojson.
6. Otevřete soubor ve VSCode a pomocí Map Preview extension zobrazte bod na mapě.

### Část B: Čtení a oprava kódu

7. Podívejte se na následující dvě funkce. U každé odpovězte: Co dělá? Má nějaký problém? Odpovědi napište jako komentáře do svého skriptu a funkce opravte.

Funkce 1:
Python

def prevod(hodnota, smer):
    if smer == "km_to_mi":
        return hodnota * 0.621371
    if smer == "mi_to_km":
        return hodnota * 1.60934

Funkce 2:
Python

souradnice = []

def pridej_bod(lat, lon):
    souradnice.append([lat, lon])
    print(f"Přidán bod: {lat}, {lon}")
    print(f"Celkem bodů: {len(souradnice)}")

---

## Odevzdání

1. Uložte všechny soubory (geodistance_prijmeni.py, misto_prijmeni.geojson).
2. Proveďte Stage, Commit (srozumitelná zpráva) a Push do své větve.
3. Vytvořte na GitHubu Pull Request do hlavní větve.

> [!tip] Tip
> Pokud si nevíte rady se syntaxí, podívejte se do materiálů k jednotlivým blokům (L5-1, L5-2, L5-3). Nezapomínejte na type hints a docstringy!

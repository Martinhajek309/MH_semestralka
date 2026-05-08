# L7: Praktická cvičení — Tuples a Sets

## Git Workflow (před začátkem)

1. **Pullněte** si nejnovější verzi repozitáře.
2. Vytvořte si novou větev ve formátu `cviceni6/prijmeni`.
3. Všechny úkoly vypracujte do složky `cviceni6/prijmeni`.

---

## Úkol 1: Tuples (Blok L7-1)

_Vytvořte skript `proda_tuples_sets_prijmeni.py`_

1. Vytvořte **seznam tuples** obsahující 10 českých měst. Každý tuple bude mít strukturu `(nazev, lat, lon, kategorie)`, kde `kategorie` je string z právě 4 možných hodnot (např. `"krajské"`, `"okresní"`, `"lázeňské"`, `"historické"`). Kategorie se mezi městy opakují.
2. Pomocí **rozbalení tuple** v cyklu vypište všechna města ve formátu: _"{nazev}: {lat}°N, {lon}°E ({kategorie})"_
3. Vytvořte funkci `je_v_oblasti(souradnice, min_lat, max_lat, min_lon, max_lon)`, která přijme tuple souřadnic `(lat, lon)` a vrátí `True`/`False` podle toho, zda bod leží v zadané oblasti.
4. Pomocí **list comprehension** a vaší funkce rozdělte města na východní a západní (zvolte vhodnou zeměpisnou délku jako hranici). Výsledky převeďte na tuples pomocí `tuple()`.

---

## Úkol 2: Sets (Blok L7-2)

_Pokračujte v souboru `proda_tuples_sets_prijmeni.py`_

1. Z východních měst vytvořte **set kategorií** a z západních měst další **set kategorií**.
2. Proiterujte se přes východní města a pro každé vypište, zda jeho kategorie existuje v setu západních kategorií (operátor `in`).
3. Pro každou unikátní kategorii ze západního setu vypište **všechna města** (východní i západní), která do ní spadají.

---

## Úkol 3: Množinové operace (Blok L7-3)

_Pokračujte v souboru `proda_tuples_sets_prijmeni.py`_

1. Vytvořte dva prázdné sety: `turisticke_atrakce` a `prirodni_rezervace`.
2. Implementujte funkci `zarad_mesto(mesto, cilovy_set)`, která přijme celý tuple města a vloží ho do zadaného setu. Zavolejte ji pro všechna města — některá zařaďte do obou setů, některá jen do jednoho.
3. Pomocí množinových operací zjistěte a vypište města, která:
   - jsou turistickou atrakcí **NEBO** přírodní rezervací (`|`)
   - jsou současně turistickou atrakcí **I** přírodní rezervací (`&`)
   - jsou turistickou atrakcí, ale **NEJSOU** přírodní rezervací (`-`)
   - jsou **BUĎ** turistickou atrakcí, **NEBO** přírodní rezervací, ale ne obojím (`^`)

---

## Odevzdání

1. Uložte soubor `proda_tuples_sets_prijmeni.py`.
2. Proveďte **Stage**, **Commit** (srozumitelná zpráva) a **Push** do své větve.
3. Vytvořte na GitHubu **Pull Request** do hlavní větve.
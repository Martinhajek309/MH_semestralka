# KGI-PRODA-2026: Python pro Geoinformatika

Vítejte v kurzu KGI-PRODA-2026. Tento dokument slouží jako základní průvodce pro práci s verzovacím systémem Git v rámci tohoto projektu.

## Co je Git?

Git **není jen "systém složek"** (jako Dropbox nebo Google Drive). Je to nástroj pro správu verzí (Version Control System).

### Klíčové principy:

- **Verzování:** Git sleduje změny v souborech v čase. Můžete se kdykoliv vrátit k předchozí verzi.
- **Větve (Branches):** V Gitu může existovat více verzí projektu najednou. Každý student pracuje ve své vlastní "větvi", čímž neovlivňuje práci ostatních ani hlavní verzi kódu.
- **Single Source of Truth:** Existuje jedna hlavní větev (zpravidla `main`), která představuje "jedinou pravdu" (funkční a schválený kód).
- **Slučování (Merge/Pull Request):** Jakmile je práce ve vaší větvi hotová a prověřená, "sloučí" se do hlavní větve. To dělá zpravidla správce (admin) po kontrole vašeho Pull Requestu.

---

## Praktické cvičení 1: Základy Gitu

Následující kroky vás provedou prvním nastavením a odevzdáním úkolu.

### 1. Příprava účtu

- Založte si účet na [GitHubu](https://github.com/) s **univerzitním e-mailem**.
- Počkejte na pozvánku do organizace/repozitáře `misavojte/KGI-PRODA-2026` a přijměte ji.

### 2. Klonování repozitáře

Otevřete terminál (nebo Git Bash) a stáhněte si projekt k sobě do počítače:

```bash
git clone https://github.com/misavojte/KGI-PRODA-2026.git
cd KGI-PRODA-2026
```

### 3. Vytvoření vlastní větve

Nikdy nepracujte přímo v hlavní větvi. Vytvořte si vlastní větev pojmenovanou podle schématu `prijmeni/cviceni1`:

```bash
git checkout -b vaseprijmeni/cviceni1
```

### 4. Splnění úkolu

1. V kořenovém adresáři najděte složku `cviceni1` (pokud neexistuje, vytvořte ji).
2. Uvnitř `cviceni1` vytvořte složku se svým příjmením (např. `cviceni1/novak`).
3. Do této složky vložte svůj `geojson` soubor z předchozího bloku.

### 5. Odeslání změn (Commit & Push)

Přidejte změny do Gitu a odešlete je na server:

```bash
git add .
git commit -m "cviceni1: odevzdani geojson souboru - Novak"
git push origin vaseprijmeni/cviceni1
```

### 6. Vytvoření Pull Requestu (PR)

1. Přejděte na stránku repozitáře na GitHubu.
2. Uvidíte žlutý pruh s tlačítkem **"Compare & pull request"** u vaší větve. Klikněte na něj.
3. Zkontrolujte, že odesíláte změny z `vaseprijmeni/cviceni1` do `main`.
4. Vytvořte Pull Request. Tím dáváte vědět vyučujícímu, že máte hotovo a vaše změny mohou být zkontrolovány a případně sloučeny.

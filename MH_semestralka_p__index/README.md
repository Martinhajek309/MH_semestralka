# Semestralni prace GIS: prostorovy index

Projekt porovnava vyhledavani bodu bez prostoroveho indexu a s jednoduchym
dlazdicovym prostorovym indexem.

## Souradnicove systemy

`data/olomoucky_kraj.geojson` je ulozen v EPSG:4326 a slouzi jako vymenny
format pro bezne GIS nastroje a webove mapy.

`data/olomoucky_kraj_5514.geojson` je ulozen v EPSG:5514
(S-JTSK / Krovak East North) a slouzi jako pracovni souradnicovy system pro
vypocty v metrech. Generovani bodu, prostorovy index a benchmark jsou
pripravene pro EPSG:5514.

Zdroj polygonu: Ceska geologicka sluzba, verejna ArcGIS REST sluzba
`Topografie/uzemni_identifikace`, vrstva `Kraje`.

## Struktura

```text
MH_semestralka_p__index/
|-- data/
|   |-- olomoucky_kraj.geojson
|   |-- olomoucky_kraj_5514.geojson
|   |-- random_points_500_olomoucky_kraj_5514.geojson
|   |-- random_points_1000_olomoucky_kraj_5514.geojson
|   |-- random_points_5000_olomoucky_kraj_5514.geojson
|   `-- random_points_olomoucky_kraj.geojson
|-- src/
|   |-- download_olomoucky_kraj.py
|   |-- generate_random_points.py
|   |-- generate_points.py
|   |-- linear_search.py
|   |-- tile_index.py
|   `-- benchmark.py
|-- results/
|   `-- benchmark_results.csv
|-- README.md
|-- requirements.txt
`-- .gitignore
```

## Spusteni

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Stazeni polygonu Olomouckeho kraje:

```powershell
python src/download_olomoucky_kraj.py
```

Vygenerovani bodu v pracovnim systemu EPSG:5514:

```powershell
python src/generate_random_points.py
```

Skript vytvori tri reprodukovatelne bodove vrstvy uvnitr skutecneho polygonu
Olomouckeho kraje: 500, 1000 a 5000 bodu. Vsechny body jsou v EPSG:5514 a maji
atributy `id`, `dataset_size`, `x` a `y`, kde `x` a `y` jsou souradnice v
metrech.

Benchmark v EPSG:5514, kde velikost dlazdice je v metrech:

```powershell
python src/benchmark.py --queries 1000 --tile-size 5000
```

Vysledky se ulozi do `results/benchmark_results.csv`.

## Benchmark vyhledavani

Skript `src/benchmark_search.py` porovnava tri metody prostoroveho vyhledavani
bodů v EPSG:5514:

- `linear_search`: pro kazdy dotaz prochazi vsechny body bez indexu.
- `tile_index`: pouziva vlastni dlazdicovy index s velikosti dlazdice 1000 m.
- `rtree_index`: pouziva prostorovy index GeoPandas/Shapely pres `gdf.sindex`.

Benchmark pouziva bodove vrstvy s 500, 1000 a 5000 body. Pro kazdy dataset
testuje 1000 nahodnych dotazovacich oken o velikostech 1000 m, 5000 m a
10000 m. Vsechny metody se kontroluji proti sobe; pokud by vratily odlisny
pocet bodu pro stejny dotaz, skript vypise chybu s konkretnim bboxem.

```powershell
python src/benchmark_search.py
```

Vysledky se ukladaji do `results/benchmark_search.csv`.

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

## Benchmark vyhledavani pro CR

Skript `src/benchmark_search_cr.py` porovnava stejne tri metody prostoroveho
vyhledavani nad bodovymi vrstvami pro celou Ceskou republiku v EPSG:5514:

- `linear_search`: pro kazdy dotaz prochazi vsechny body bez indexu.
- `tile_index`: pouziva vlastni dlazdicovy index s velikosti dlazdice 5000 m.
- `rtree_index`: pouziva knihovni prostorovy index GeoPandas/Shapely pres
  `gdf.sindex`.

Benchmark pouziva datasety s 5000, 10000 a 50000 body. Pro kazdy dataset
testuje 1000 nahodnych dotazovacich oken o velikostech 5000 m, 20000 m a
50000 m. Pro vsechny metody se pouziva stejna sada dotazu a vysledky se
kontroluji proti sobe.

```powershell
python src/benchmark_search_cr.py
```

Vysledky se ukladaji do `results/benchmark_search_cr.csv`.

## Radius query

Radius query je prostorovy dotaz, ktery pro zadany dotazovaci bod hleda vsechny
body do urcite vzdalenosti. V tomto projektu se radius query pocita v EPSG:5514,
protoze souradnice jsou v metrech a eukleidovska vzdalenost tak odpovida
testovanym polomerum 5000 m, 10000 m a 25000 m.

Skript `src/benchmark_radius_query_cr.py` porovnava tri pristupy nad bodovymi
vrstvami pro celou Ceskou republiku:

- `linear_search_radius`: pro kazdy dotaz projde vsechny body a primo spocita
  vzdalenost od dotazovaciho bodu.
- `tile_index_radius`: body jsou rozdelene do dlazdic o velikosti 5000 m.
  Dotaz nejdrive vybere dlazdice protinajici bbox kruznice a potom kandidaty
  presne overi eukleidovskou vzdalenosti.
- `rtree_index_radius`: knihovni index GeoPandas/Shapely `gdf.sindex` nejdrive
  najde kandidaty v bboxu kruznice a kandidati se potom presne overi
  vzdalenosti.

Kandidati z indexu nejsou sami o sobe vysledkem radius query. U dlazdicoveho i
R-tree / STRtree indexu se musi jeste presne overit, ze jejich vzdalenost od
dotazovaciho bodu je mensi nebo rovna zadanemu polomeru.

```powershell
python src/benchmark_radius_query_cr.py
```

Vysledky se ukladaji do `results/benchmark_radius_query_cr.csv`.

## Polygon query

Polygon query hleda body lezici uvnitr nepravidelneho polygonu. V tomto
benchmarku je dotazovacim polygonem vzdy jeden skutecny kraj Ceske republiky a
vysledkem je pocet bodu bodove vrstvy, ktere lezi uvnitr jeho hranice.

Tento dotaz je jiny nez vyhledavani ve ctvercovem okne: ctvercove okno ma
jednoduchy bbox, zatimco kraj ma nepravidelny tvar. Proto se index pouzije jen
pro vyber kandidatnich bodu podle bounding boxu polygonu a kandidati se potom
musi presne overit vuci skutecnemu tvaru kraje.

Skript `src/benchmark_polygon_query_cr.py` pouziva skutecne hranice 14 kraju CR.
Pokud nejsou ulozene v `data/kraje_cr_5514.geojson`, pokusi se najit lokalni
vrstvu vsech kraju, jinak je stahne z verejne ArcGIS REST sluzby Ceske
geologicke sluzby `Topografie/uzemni_identifikace`, vrstva `Kraje`. Vystupy
vrstvy kraju jsou `data/kraje_cr.geojson` v EPSG:4326 a
`data/kraje_cr_5514.geojson` v EPSG:5514.

Vypocty probiha v EPSG:5514, protoze jde o pracovni souradnicovy system v
metrech. Benchmark porovnava:

- `linear_search_polygon`: pro kazdy kraj projde vsechny body a presne testuje,
  zda bod lezi uvnitr polygonu.
- `tile_index_polygon`: body jsou ulozene ve vlastnim dlazdicovem indexu s
  dlazdici 5000 m; pro kraj se nejdrive vyberou dlazdice podle bboxu a potom se
  kandidati presne overi vuci polygonu kraje.
- `rtree_index_polygon`: GeoPandas/Shapely `gdf.sindex` vybere kandidaty podle
  bboxu polygonu a kandidati se potom presne overi vuci skutecne geometrii
  kraje.

```powershell
python src/benchmark_polygon_query_cr.py
```

Souhrn benchmarku se uklada do `results/benchmark_polygon_query_cr.csv` a
detailni pocty podle kraju do `results/polygon_query_counts_by_kraj.csv`.

## Polygon Ceske republiky

Skript `src/prepare_ceska_republika_polygon.py` pripravuje polygon cele Ceske
republiky pro doplnkovy benchmark prostorovych indexu. Pokud je ve slozce
`data/` dostupna vrstva vsech kraju, skript ji pouzije; jinak stahne kraje z
verejne ArcGIS REST sluzby Ceske geologicke sluzby
`Topografie/uzemni_identifikace`, vrstva `Kraje`.

Polygon Ceske republiky vznikne sjednocenim geometrii kraju do jednoho prvku.
Soubor `data/ceska_republika.geojson` je ulozen v EPSG:4326 jako vymenny
format. Soubor `data/ceska_republika_5514.geojson` je ulozen v EPSG:5514 a
slouzi pro vypocty a benchmark v metrech.

```powershell
python src/prepare_ceska_republika_polygon.py
```

## Bodove vrstvy Ceske republiky

Skript `src/generate_random_points_cr.py` generuje reprodukovatelne nahodne
bodove vrstvy uvnitr skutecneho polygonu Ceske republiky v EPSG:5514. Vytvari
datasety s 5000, 10000 a 50000 body:

- `data/random_points_5000_cr_5514.geojson`
- `data/random_points_10000_cr_5514.geojson`
- `data/random_points_50000_cr_5514.geojson`

Kazdy bod ma atributy `id`, `dataset_size`, `area_name`, `x` a `y`.
Hodnota `area_name` je `Ceska republika` a souradnice `x`, `y` jsou ulozene v
metrech v EPSG:5514. Kandidatni body se generuji z bounding boxu, ale kazdy bod
je pred ulozenim overen proti skutecnemu polygonu CR.

```powershell
python src/generate_random_points_cr.py
```

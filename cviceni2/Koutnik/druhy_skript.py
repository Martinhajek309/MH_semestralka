#!/usr/bin/env python3
# ============================================================
# PRODA 2026 – Programové zpracování dat
# Thiessenovy polygony: Která část ČR patří ke kterému městu?
# ============================================================
# NEMĚNIT ORIGINÁLNÍ SOUBOR! 
# Pracujte na své nové větvi a upravujte kopii ve složce /vaseprijmeni.
# ============================================================
# Upravujte pak kopii, jinak dojde ke git konfliktu a nepůjde
# vám odevzdat úkol.
# ============================================================
# Tento skript vypočítá a vykreslí Thiessenovy (Voronoi) polygony
# pro největší česká města a uloží výsledek jako obrázek.
#
# ⚠️  Ke spuštění potřebujete nainstalovat knihovny!
#     1. Vytvořte si virtuální prostředí
#     2. Aktivujte hoe
#     3. Nainstalujte knihovny
#     4. Spusťte skript
# ============================================================

import os
import sys
import subprocess
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import geopandas as gpd
from shapely.geometry import MultiPoint, Point, box
from shapely.ops import voronoi_diagram

# ============================================================
# 1. Stažení hranice České republiky
# ============================================================
# Použijeme dataset Natural Earth — volně dostupná geodata pro celý svět.
# Stáhneme soubor zemí světa a vyfiltrujeme si Českou republiku.

print("⬇️  Stahuji hranici ČR z Natural Earth...")

URL_NATURAL_EARTH = (
    "https://naturalearth.s3.amazonaws.com"
    "/50m_cultural/ne_50m_admin_0_countries.zip"
)

svet = gpd.read_file(URL_NATURAL_EARTH)                 # Celý svět
cr = svet[svet["ISO_A3"] == "CZE"].to_crs(epsg=4326)   # Filtr: jen ČR, WGS 84
cr_geom = cr.geometry.union_all()                       # Spojení do jednoho polygonu

print("✅ Hranice ČR načtena!\n")

# ============================================================
# 2. Data: největší česká města
# ============================================================

mesta = [
    {"nazev": "Praha",            "lon": 14.4378, "lat": 50.0755, "pop": 1_309_000},
    {"nazev": "Brno",             "lon": 16.6068, "lat": 49.1951, "pop":   382_000},
    {"nazev": "Ostrava",          "lon": 18.2625, "lat": 49.8209, "pop":   284_000},
    {"nazev": "Plzeň",            "lon": 13.3736, "lat": 49.7384, "pop":   174_000},
    {"nazev": "Liberec",          "lon": 15.0562, "lat": 50.7671, "pop":   104_000},
    {"nazev": "Olomouc",          "lon": 17.2509, "lat": 49.5938, "pop":   101_000},
    {"nazev": "České Budějovice", "lon": 14.4744, "lat": 48.9745, "pop":    94_000},
    {"nazev": "Hradec Králové",   "lon": 15.8327, "lat": 50.2092, "pop":    92_000},
    {"nazev": "Ústí nad Labem",   "lon": 14.0416, "lat": 50.6607, "pop":    91_000},
    {"nazev": "Pardubice",        "lon": 15.7696, "lat": 50.0343, "pop":    91_000},
    {"nazev": "Zlín",             "lon": 17.6647, "lat": 49.2261, "pop":    72_000},
    {"nazev": "Jihlava",          "lon": 15.5896, "lat": 49.3961, "pop":    51_000},
]

# ============================================================
# 3. Výpočet Thiessenových polygonů
# ============================================================
# Thiessenova tessellation = pro každý bod plocha, která je
# nejblíže právě jemu (a ne jinému bodu).

print("📐 Počítám Thiessenovy polygony...")

# Vytvoříme shapely objekt se všemi body měst
souradnice = [(m["lon"], m["lat"]) for m in mesta]
body = MultiPoint(souradnice)

# Voronoi diagram s obálkou přesahující ČR (jinak by krajní polygony
# sahaly do nekonečna)
obalka = box(10.5, 47.5, 20.0, 52.0)
voronoi = voronoi_diagram(body, envelope=obalka)

# Přiřadíme každý Voronoi polygon k městu (hledáme, které město leží uvnitř)
# a ořízněme polygon na hranici ČR
prirazene_polygony = []

for polygon in voronoi.geoms:
    for i, (lon, lat) in enumerate(souradnice):
        if polygon.contains(Point(lon, lat)):
            oriznuty = polygon.intersection(cr_geom)    # Ořez na ČR ✂️
            prirazene_polygony.append({
                "polygon": oriznuty,
                "mesto": mesta[i],
            })
            break

print(f"✅ Vypočítáno {len(prirazene_polygony)} polygonů.\n")

# ============================================================
# 4. Vizualizace
# ============================================================

print("🎨 Vykresluji mapu...")

fig, ax = plt.subplots(figsize=(14, 9))
fig.patch.set_facecolor("#0f0f1a")
ax.set_facecolor("#0f0f1a")

# Barevná paleta
barvy = plt.cm.tab20(np.linspace(0, 1, len(mesa := prirazene_polygony)))

# Vykreslíme Thiessenovy polygony
for i, prvek in enumerate(prirazene_polygony):
    polygon = prvek["polygon"]
    if polygon.is_empty:
        continue

    geo = gpd.GeoSeries([polygon])
    geo.plot(
        ax=ax,
        color=barvy[i],
        alpha=0.55,
        edgecolor="white",
        linewidth=0.8,
    )

# Obrys ČR přes to — výrazná bílá hranice
cr.boundary.plot(ax=ax, color="white", linewidth=2.0, zorder=10)

# Markery měst — velikost podle populace
populace = np.array([p["mesto"]["pop"] for p in prirazene_polygony])
velikosti = (populace / populace.max()) * 350 + 30

for i, prvek in enumerate(prirazene_polygony):
    m = prvek["mesto"]
    ax.scatter(
        m["lon"], m["lat"],
        s=velikosti[i],
        color=barvy[i],
        edgecolors="white",
        linewidths=1.2,
        zorder=20,
    )
    ax.annotate(
        m["nazev"],
        xy=(m["lon"], m["lat"]),
        xytext=(5, 4),
        textcoords="offset points",
        color="white",
        fontsize=8,
        fontweight="bold",
        zorder=21,
    )

# Titulek a osy
ax.set_title(
    "Thiessenovy polygony — největší česká města\n"
    "Každá oblast je nejblíže danému městu",
    color="white",
    fontsize=13,
    pad=14,
)
ax.set_xlabel("Zeměpisná délka (°E)", color="#aaaacc", fontsize=9)
ax.set_ylabel("Zeměpisná šířka (°N)", color="#aaaacc", fontsize=9)
ax.tick_params(colors="#aaaacc")
for spine in ax.spines.values():
    spine.set_edgecolor("#333355")

# Legenda
legenda = [
    mpatches.Patch(
        facecolor=barvy[i],
        alpha=0.7,
        label=f"{p['mesto']['nazev']} ({p['mesto']['pop'] // 1000} tis.)",
    )
    for i, p in enumerate(prirazene_polygony)
]
ax.legend(
    handles=legenda,
    loc="lower left",
    fontsize=7.5,
    framealpha=0.3,
    labelcolor="white",
    facecolor="#1a1a2e",
    edgecolor="#333355",
    ncol=2,
)

plt.tight_layout()

# ============================================================
# 5. Uložení a otevření výsledku
# ============================================================

adresar_skriptu = os.path.dirname(os.path.abspath(__file__))
vystupni_soubor = os.path.join(adresar_skriptu, "thiessenovy_polygony.png")

plt.savefig(
    vystupni_soubor,
    dpi=150,
    bbox_inches="tight",
    facecolor=fig.get_facecolor(),
)
print(f"✅ Obrázek uložen: {vystupni_soubor}")

# Otevřeme obrázek v systémovém prohlížeči
if sys.platform == "win32":
    os.startfile(vystupni_soubor)
elif sys.platform == "darwin":
    subprocess.run(["open", vystupni_soubor])
else:
    subprocess.run(["xdg-open", vystupni_soubor])

print("🗺️  Hotovo!")

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import geopandas as gpd
from shapely.geometry import MultiPoint, Point, box
from shapely.ops import voronoi_diagram

# OPRAVA PRO TVÉ PROSTŘEDÍ (Windows + nová verze Pythonu)
gpd.options.io_engine = "pyogrio"

# ============================================================
# 1. Data: největší česká města
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
# 2. Výpočet Thiessenových polygonů
# ============================================================

print("📐 Počítám Thiessenovy polygony...")

souradnice = [(m["lon"], m["lat"]) for m in mesta]
body = MultiPoint(souradnice)

# Obálka nastavena na rozsah ČR
obalka = box(12.0, 48.5, 19.0, 51.1)
voronoi = voronoi_diagram(body, envelope=obalka)

prirazene_polygony = []

for polygon in voronoi.geoms:
    for i, (lon, lat) in enumerate(souradnice):
        if polygon.contains(Point(lon, lat)):
            # TADY JSME ODSTRANILI OŘEZ PODLE HRANIC ČR (intersection)
            prirazene_polygony.append({
                "polygon": polygon,
                "mesto": mesta[i],
            })
            break

print(f"✅ Vypočítáno {len(prirazene_polygony)} polygonů.\n")

# ============================================================
# 3. Vizualizace
# ============================================================

print("🎨 Vykresluji mapu...")

fig, ax = plt.subplots(figsize=(14, 9))
fig.patch.set_facecolor("#0f0f1a")
ax.set_facecolor("#0f0f1a")

barvy = plt.cm.tab20(np.linspace(0, 1, len(prirazene_polygony)))

for i, prvek in enumerate(prirazene_polygony):
    geo = gpd.GeoSeries([prvek["polygon"]])
    geo.plot(
        ax=ax,
        color=barvy[i],
        alpha=0.55,
        edgecolor="white",
        linewidth=0.8,
    )

# Markery měst
populace = np.array([p["mesto"]["pop"] for p in prirazene_polygony])
velikosti = (populace / populace.max()) * 350 + 30

for i, prvek in enumerate(prirazene_polygony):
    m = prvek["mesto"]
    ax.scatter(m["lon"], m["lat"], s=velikosti[i], color=barvy[i], 
               edgecolors="white", linewidths=1.2, zorder=20)
    ax.annotate(m["nazev"], xy=(m["lon"], m["lat"]), xytext=(5, 4),
                textcoords="offset points", color="white", fontsize=8, 
                fontweight="bold", zorder=21)

ax.set_title("Thiessenovy polygony — největší česká města", color="white", fontsize=13, pad=14)
ax.set_axis_off() # Vypneme osy, aby to vypadalo jako čistá mapa

# Legenda
legenda = [mpatches.Patch(facecolor=barvy[i], alpha=0.7, 
           label=f"{p['mesto']['nazev']}") for i, p in enumerate(prirazene_polygony)]
ax.legend(handles=legenda, loc="lower left", fontsize=7.5, framealpha=0.3, 
          labelcolor="white", facecolor="#1a1a2e", ncol=2)

# ============================================================
# 4. Uložení
# ============================================================

vystupni_soubor = "thiessenovy_polygony.png"
plt.savefig(vystupni_soubor, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
print(f"✅ Obrázek uložen: {vystupni_soubor}")

# Otevření obrázku
if sys.platform == "win32":
    os.startfile(vystupni_soubor)

print("🗺️  Hotovo bez stahování z internetu!")
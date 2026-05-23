# ============================================================
# PRODA 2026 – Programové zpracování dat
# Úvodní skript: Města České republiky
# ============================================================
# NEMĚNIT ORIGINÁLNÍ SOUBOR! 
# Pracujte na své nové větvi a upravujte kopii ve složce /vaseprijmeni.
# ============================================================
# Upravujte pak kopii, jinak dojde ke git konfliktu a nepůjde
# vám odevzdat úkol.
# ============================================================
# Tento skript ukazuje, co Python dokáže v pár řádcích.
# Vaším úkolem je najít a opravit všechny SYNTAKTICKÉ chyby,
# které VS Code označí červeně.
# ============================================================

# --- 1. Základní informace o městech ---

mesta = [
    {"nazev": "Praha", "populace": 1_309_000, "souradnice": [50.0755, 14.4378]},
    {"nazev": "Brno", "populace": 382_000, "souradnice": [49.1951, 16.6068]},
    {"nazev": "Ostrava", "populace": 284_000,  "souradnice": [49.8209, 18.2625]},
    {"nazev": "Plzeň", "populace": 174_000, "souradnice": [49.7384, 13.3736]},
    {"nazev": "Olomouc", "populace": 101_000, "souradnice": [49.5938, 17.2509]},
]

# --- 2. Výpis informací o městech ---

print("=== Města České republiky ===")
print()

for mesto in mesta:
    nazev = mesto["nazev"]
    populace = mesto["populace"]
    lat = mesto["souradnice"][0]
    lon = mesto["souradnice"][1]
    
    print(f"{nazev}: {populace} obyvatel")
    print(f"  Souřadnice: {lat}° N, {lon}° E")
    print()

# --- 3. Najdeme největší město ---

nejvetsi = mesta[0]

for mesto in mesta:
    if mesto["populace"] > nejvetsi["populace"]:
        nejvetsi = mesto

print(f"Největší město: {nejvetsi['nazev']} ({nejvetsi['populace']} obyvatel)")
print()

# --- 4. Výpočet celkové populace ---

celkova_populace = 0

for mesto in mesta:
    celkova_populace += mesto["populace"]

print(f"Celková populace sledovaných měst: {celkova_populace}")
print()

# --- 5. Průměrná zeměpisná šířka ---

soucet_lat = 0

for mesto in mesta:
    soucet_lat += mesto["souradnice"][0]

prumerna_lat = soucet_lat / len(mesta)
print(f"Průměrná zeměpisná šířka: {prumerna_lat:.4f}° N")
print()

# --- 6. Která města mají více než 200 000 obyvatel? ---

print("Města nad 200 000 obyvatel:")

for mesto in mesta:
    if mesto["populace"] > 200_000:
        print(f"  ✓ {mesto['nazev']}")
    else:
        print(f"  ✗ {mesto['nazev']}")

print()

# --- 7. Vzdálenost měst od Prahy (zjednodušený odhad) ---

praha_lat = mesta[0]["souradnice"][0]
praha_lon = mesta[0]["souradnice"][1]

print("Přibližná vzdálenost od Prahy:")

for mesto in mesta[1:]:
    nazev = mesto["nazev"]
    lat = mesto["souradnice"][0]
    lon = mesto["souradnice"][1]
    
    # Zjednodušený výpočet (rozdíl souřadnic × přibližný převod na km)
    vzdalenost = ((lat - praha_lat) ** 2 + (lon - praha_lon) ** 2) ** 0.5 * 111
    
    print(f"  {nazev}: ~{vzdalenost:.0f} km")

print()
print("Hotovo! 🎉")




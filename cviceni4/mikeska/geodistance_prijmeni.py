

def vypocitej_vzdalenost_od_rovniku(sirka):
    """Vypočítá vzdálenost od rovníku na základě zeměpisné šířky."""
    KM_NA_STUPEN = 111.32
    vzdalenost = abs(sirka) * KM_NA_STUPEN
    print(f"Město na šířce {sirka}° je {vzdalenost:.2f} km od rovníku.")
    return vzdalenost


sirky = [0, 15, 30, 45, 60]

for sirka in sirky:
    vypocitej_vzdalenost_od_rovniku(sirka)
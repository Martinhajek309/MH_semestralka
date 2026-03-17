

def vypocitej_vzdalenost_od_rovniku(sirka: float, jednotka: str = "km", zaokrouhlit: bool = True) -> float:
   
    KM_NA_STUPEN = 111.32
    KM_NA_MILI = 0.621371
    
    vzdalenost = abs(sirka) * KM_NA_STUPEN
    
    if jednotka == "míle":
        vzdalenost *= KM_NA_MILI
    
    if zaokrouhlit:
        vzdalenost = round(vzdalenost)
    
    return vzdalenost



sirky = [0, 1234.4, 30.43434, 45.2 , 60.5, 90]

print("=== Vzdálenosti v kilometrech ===")
for sirka in sirky:
    vzdalenost = vypocitej_vzdalenost_od_rovniku(sirka, jednotka="km")
    print(f"Město na šířce {sirka}° je {vzdalenost} km od rovníku.")
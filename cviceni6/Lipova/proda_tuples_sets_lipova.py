mesta_tuples = tuple([("Praha", 50.073658, 14.418540, 'krajské'), 
                      ("Brno", 49.199980, 16.608220, 'krajské'), 
                      ("Ostrava", 49.793230, 18.122730, 'krajské'), 
                      ("Plzeň", 49.738370, 13.376520, 'krajské'), 
                      ("Liberec", 50.782650, 15.064620, 'krajské'),
                        ("Kyjov", 48.846110, 17.122220, 'historické'),
                        ("Hodonín", 48.850000, 17.132220, 'okresní'),
                        ("Znojmo", 48.855000, 16.048220, 'historické'),
                        ("Břeclav", 48.758330, 16.882220, 'okresní'),
                        ("Luhačovice", 49.132220, 17.666670, 'lázeňské')])

for mesto, lat, lon, typ in mesta_tuples:
    print(f"{mesto} se nachází na souřadnicích {lat}°N, {lon}°E a je to {typ} město.")

def je_v_oblasti(souradnice, min_lat, max_lat, min_lon, max_lon):
    lat, lon = souradnice
    return min_lat <= lat <= max_lat and min_lon <= lon <= max_lon

vychodni_mesta = tuple([m for m in mesta_tuples if je_v_oblasti((m[1], m[2]), -90, 90, 15, 180)])
zapadni_mesta = tuple([m for m in mesta_tuples if je_v_oblasti((m[1], m[2]), -90, 90, -180, 15)])

print("\nVýchodní města (východně od 15°E):")
for m in vychodni_mesta: print(m[0])
print("\nZápadní města (západně od 15°E):")
for m in zapadni_mesta: print(m[0])

## Úkol 2: Sets (Blok L7-2)
vychodni = set(m[3] for m in vychodni_mesta)
zapadni = set(m[3] for m in zapadni_mesta)
print(f"Kategorie východních měst: {vychodni}")
print(f"Kategorie západních měst: {zapadni}")

for m in vychodni_mesta:
    mesto_nazev = m[0]
    mesto_kat = m[3]
    
    if mesto_kat in zapadni:
        print(f"Město {mesto_nazev} má kategorii '{mesto_kat}', která je i na západě.")
    else:
        print(f"Město {mesto_nazev} má kategorii '{mesto_kat}', která se na západě NEVYSKYTUJE.")

vsechna_mesta = vychodni_mesta + zapadni_mesta

for kat in zapadni:
    mesta_v_kategorii = [m[0] for m in vsechna_mesta if m[3] == kat]
    print(f"Kategorie '{kat}': {', '.join(mesta_v_kategorii)}")

## Úkol 3: Množinové operace (Blok L7-3)

turisticke_atrakce = set()
prirodni_rezervace = set()

def zarad_mesto(mesto_tuple, cilovy_set):
    cilovy_set.add(mesto_tuple)

zarad_mesto(mesta_tuples[0], turisticke_atrakce) # Praha
zarad_mesto(mesta_tuples[0], prirodni_rezervace) 

zarad_mesto(mesta_tuples[9], turisticke_atrakce) # Luhačovice
zarad_mesto(mesta_tuples[9], prirodni_rezervace)

zarad_mesto(mesta_tuples[1], turisticke_atrakce) # Brno
zarad_mesto(mesta_tuples[3], turisticke_atrakce) # Plzeň
zarad_mesto(mesta_tuples[5], turisticke_atrakce) # Kyjov
zarad_mesto(mesta_tuples[7], turisticke_atrakce) # Znojmo

zarad_mesto(mesta_tuples[2], prirodni_rezervace) # Ostrava
zarad_mesto(mesta_tuples[4], prirodni_rezervace) # Liberec
zarad_mesto(mesta_tuples[6], prirodni_rezervace) # Hodonín
zarad_mesto(mesta_tuples[8], prirodni_rezervace) # Břeclav

sjednoceni = turisticke_atrakce | prirodni_rezervace
print(f"\nSjednocení turistických atrakcí a přírodních rezervací: {sjednoceni}")
prunik = turisticke_atrakce & prirodni_rezervace
print(f"Průnik turistických atrakcí a přírodních rezervací: {prunik}")
rozdil = turisticke_atrakce - prirodni_rezervace
print(f"Rozdíl turistických atrakcí a přírodních rezervací: {rozdil}")  
symetricky_rozdil = turisticke_atrakce ^ prirodni_rezervace
print(f"Symetrický rozdíl turistických atrakcí a přírodních rezervací: {symetricky_rozdil}")    
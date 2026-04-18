teploty = [
	2.5, 2.0, 85.5, 1.5, -25.0, 0.5, 0.0, -0.8,
	-1.2, -0.4, 1.0, 2.3, 3.8, 4.6, 5.2, 5.8,
	6.0, 5.5, 4.9, 4.0, 3.3, 2.7, 2.2, 1.8,
]

print("Kontrola měření z 1. února 2024...")

zpracovana_mereni = 0

for hodina, teplota in enumerate(teploty, start=1):
	if teplota > 50:
		print(f"Teplota ve {hodina}:00 je {teplota}°C >>> Přeskakuji, káva na senzoru!")
		continue

	if teplota < -20:
		print(f"Teplota ve {hodina}:00 je {teplota}°C >>> Senzor se rozbil, končím!")
		break

	print(f"Teplota ve {hodina}:00 je {teplota}°C")
	zpracovana_mereni += 1

print(f"Zpracováno měření: {zpracovana_mereni}")

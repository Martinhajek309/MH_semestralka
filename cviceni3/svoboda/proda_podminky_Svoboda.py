try:
	teplota = float(input("Zadejte teplotu ve °C: "))
	vlhkost = float(input("Zadejte vlhkost v %: "))

	if vlhkost < 0 or vlhkost > 100:
		print("Chyba: Vlhkost musí být v rozsahu 0-100 %.")
	else:
		if teplota < 0:
			klasifikace = "Mrzne"
		elif teplota < 10:
			klasifikace = "Zima"
		elif teplota < 20:
			klasifikace = "Jaro/Podzim"
		elif teplota <= 30:
			klasifikace = "Léto"
		else:
			klasifikace = "Vedro"

		print(f"Klasifikace teploty: {klasifikace}")

		if teplota > 25 and vlhkost > 70:
			print("Tropické počasí")

except ValueError:
	print("Chyba: Zadejte číselné hodnoty pro teplotu i vlhkost.")

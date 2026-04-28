
mesto = "Praha"
souradnice = [50.0755, 14.4378]  
obyvatel = 1335000              
rozloha = 496.21                
je_hlavni = True               

hustota = obyvatel / rozloha

print(f"Typ 'mesto': {type(mesto)}")
print(f"Typ 'souradnice': {type(souradnice)}")
print(f"Typ 'obyvatel': {type(obyvatel)}")
print(f"Typ 'rozloha': {type(rozloha)}")
print(f"Typ 'je_hlavni': {type(je_hlavni)}")

jmeno = input("Zadej své jméno: ")

print(f"Ahoj {jmeno}, město {mesto} má hustotu {hustota:.2f} obyv./km² a nachází se na souřadnicích {souradnice}.")
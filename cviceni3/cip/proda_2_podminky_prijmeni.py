temp = input("Input current temperature: ")
temp_float = float(temp)

if temp_float > 35:
    print("It's hot outside!")
elif temp_float > 30:
    print("It's warm outside!")
elif temp_float > 20:
    print("It's nice outside!")
else:
    print("Fly to Spain!")
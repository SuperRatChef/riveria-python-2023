# Kirjoita ratkaisu tähän
num1 = int(input("Luku 1:"))
num2 = int(input("Luku 2:"))
command = input("Komento:")
result = 0

if(command == "summa"):
    result = num1 + num2
    print(f"{num1} + {num2} = {num1+num2}")
if(command == "tulo"):
    result = num1 * num2
    print(f"{num1} * {num2} = {num1*num2}")
if(command == "erotus"):
    result = num1 - num2
    print(f"{num1} - {num2} = {num1-num2}")

# Kirjoita ratkaisu tähän
num1 = int(input("Anna ensimmäinen luku:"))
num2 = int(input("Anna toinen luku:"))
 
if(num1 < num2):
    print("Suurempi luku:",num2)
elif(num2 < num1):
    print("Suurempi luku:", num1)
else:
    print("Luvut ovat yhtä suuret!")
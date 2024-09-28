# Kirjoita ratkaisu tähän
salasana = input("Salasana: ")
varmistus = input("Toista salasana: ")


while(salasana != varmistus):
    print("Ei ollut sama!")
    varmistus = input("Toista salasana: ")

print("Käyttäjätunnus luotu!")
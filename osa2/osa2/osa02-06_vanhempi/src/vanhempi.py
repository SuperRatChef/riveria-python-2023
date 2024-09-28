# Kirjoita ratkaisu tähän

print("Henkilö 1:")
nimi1 = input("Nimi: ")
ika1 = int(input("Ikä: "))
print("Henkilö 2:")
nimi2 = input("Nimi: ")
ika2 = int(input("Ikä: "))

if(ika1 < ika2):
    print("Vanhempi on", nimi2)
elif(ika2 < ika1):
    print("Vanhempi on", nimi1)
else:
    print(f"{nimi1} ja {nimi2} ovat yhtä vanhoja")

# Kirjoita ratkaisu tähän
sana = input("Sana: ")
merkki = input("Merkki: ")

alku = sana.find(merkki)
loppu = alku+3

if(not loppu >= len(sana)):
    print(sana[alku:loppu])
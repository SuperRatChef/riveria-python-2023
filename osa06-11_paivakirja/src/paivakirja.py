# tee ratkaisu tänne
print("1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta")
valinta = int(input("Valinta: "))
while(valinta != 0):
    if(valinta == 1):
        merkinta = input("Anna merkintä: ")
        with open("paivakirja.txt", "a") as tiedosto:
            tiedosto.write(f"{merkinta}\n")
        print("Päiväkirja tallennettu")
        print("")
    elif(valinta == 2):
        with open("paivakirja.txt") as tiedosto:
            for rivi in tiedosto:
                print(rivi)
    print("1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta")
    valinta = int(input("Valinta: "))

print("Heippa!")
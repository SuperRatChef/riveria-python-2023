# Kirjoita ratkaisu tähän
sana = input("Sana: ")
merkki = input("Merkki: ")


while True:
    alku = sana.find(merkki)
    loppu = alku+3
    
    if(alku == -1):
        break
    if len(sana)-alku < 3 or len(sana) < 3:
        break
    if(loppu >= len(sana)):
        loppu = len(sana)

    #print(sana)

    print(sana[alku:loppu])
    sana = sana[alku+1:]
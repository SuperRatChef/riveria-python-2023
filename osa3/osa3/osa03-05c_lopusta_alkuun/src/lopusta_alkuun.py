# Kirjoita ratkaisu tähän

merkkijono = input("Anna merkkijono: ")
aloitusIndex = len(merkkijono)-1
lopetusIndex = 0
iteraattori = aloitusIndex

while(iteraattori >= lopetusIndex):
    print(merkkijono[iteraattori])
    iteraattori -= 1
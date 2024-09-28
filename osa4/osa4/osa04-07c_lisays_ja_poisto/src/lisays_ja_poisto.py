# Kirjoita ratkaisu tähän
valinta = ""
lista = []
while(valinta != "x"):
    print(f"Lista on nyt {lista}")
    valinta = input("(l)isää, (p)oista vai e(x)it: ").lower()
    if(valinta == "l"):
        lista.append(len(lista)+1)
    elif(valinta == "p"):
        lista.pop()
    
print("Moi!")

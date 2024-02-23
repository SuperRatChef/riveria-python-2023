# Kirjoita ratkaisu tähän
lista = []

luku = 1
while(luku != 0):
    luku = int(input("Anna luku: "))
    if(luku == 0):
        break
    else:
        lista.append(luku)
        print(f"Lista: {lista}")
        print(f"Järjestettynä: {sorted(lista)}")
print("Moi!")


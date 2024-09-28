# Kirjoita ratkaisu tähän
n = int(input("Mihin asti: "))
iterator = 1
summa = 0
luvut = []
while(summa < n):
    summa += iterator
    luvut.append(iterator)
    iterator += 1
    
print(f"Laskettiin {" + ".join([str(luku) for luku in luvut])} = {summa}")
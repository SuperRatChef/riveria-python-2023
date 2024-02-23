# Kirjoita ratkaisu tähän
luvut = []
print("Syötä kokonaislukuja, 0 lopettaa:")
while(True):
    luku = int(input("Luku: "))
    if(luku == 0):
        break
    else:
        luvut.append(luku)

print(f"Lukuja yhteensä {len(luvut)}")
print(f"Lukujen summa {sum(luvut)}")
print(f"Lukujen keskiarvo {sum(luvut) / len(luvut)}")
positiiviset = 0
negatiiviset = 0
for luku in luvut:
    if(luku < 0):
        negatiiviset += 1
    else:
        positiiviset += 1

print("Positiivisia",positiiviset)
print("Negatiivisia",negatiiviset)



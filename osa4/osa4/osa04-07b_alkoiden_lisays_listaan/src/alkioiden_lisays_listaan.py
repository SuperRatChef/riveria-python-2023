# Kirjoita ratkaisu tähän
kuinka_monta_lukua = int(input("Kuinka monta lukua: "))
iteraattori = 1
arr = []
while(iteraattori <= kuinka_monta_lukua):
    luku = int(input(f"Anna luku {iteraattori}: "))
    arr.append(luku)
    iteraattori += 1
print(arr)
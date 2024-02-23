# Kirjoita ratkaisu tähän
arr = [1, 2, 3, 4, 5]
indeksi = int(input("Anna indeksi: "))
while(indeksi != -1):
    arvo = int(input("Anna arvo: "))
    arr[indeksi] = arvo
    print(arr)
    indeksi = int(input("Anna indeksi:"))
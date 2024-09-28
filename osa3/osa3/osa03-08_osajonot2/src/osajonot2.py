# Kirjoita ratkaisu tähän
merkkijono = input("Anna merkkijono: ")

for i in range(len(merkkijono)+1, -1, -1):
    print(merkkijono[i:])
# Kirjoita ratkaisu tähän

c1 = input("Anna 1. kirjain: ")
c2 = input("Anna 2. kirjain: ")
c3 = input("Anna 3. kirjain: ")

arr = [c1, c2, c3]

arr.sort()
print(f"Keskimmäinen kirjain on {arr[1]}")
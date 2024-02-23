# Kirjoita ratkaisu tähän

n = int(input("Anna luku: "))

for i in range(1, n+1):
    for j in range(1, n+1):
        print(f"{i} x {j} = {i*j}")
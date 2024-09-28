# Kirjoita ratkaisu tähän


n = int(input("Anna luku")) 
while(n > 0): 
    i = 1
    kertoma = 1
    while(i <= n and n > 0):
        kertoma *= i
        i += 1
    print(f"Luvun {n} kertoma on {kertoma}")
    n = int(input("Anna luku"))

print("Kiitos ja moi!")


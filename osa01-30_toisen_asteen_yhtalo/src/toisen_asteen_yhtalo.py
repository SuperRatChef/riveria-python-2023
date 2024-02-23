# Kirjoita ratkaisu tähän
# Otetaan käyttöön neliöjuuri math-moduulista
from math import sqrt

# Huomaa, että neliöjuuren voi laskea myös potenssin avulla:
# sqrt(9) on sama asia kuin 9 ** 0.5

a = int(input("Anna a:"))
b = int(input("Anna b:"))
c = int(input("Anna c:"))

x1 = (-b + sqrt(b**2-4*a*c))/(2*a)
x2 = (-b - sqrt(b**2-4*a*c))/(2*a)

print("Juure ovat",x1,"ja",x2)
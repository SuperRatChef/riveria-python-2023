# tee ratkaisu tähän
def tulosta_monesti(merkkijono, kertaa):
    iteraattori = 1
    while(iteraattori <= kertaa):
        print(merkkijono)
        iteraattori += 1
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    tulosta_monesti("python", 5)
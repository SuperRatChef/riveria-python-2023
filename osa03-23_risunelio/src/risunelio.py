# tee ratkaisu tänne
def risunelio(koko):
    korkeus = 1
    while(korkeus <= koko):
        print("#"*koko)
        korkeus += 1
            
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risunelio(5)
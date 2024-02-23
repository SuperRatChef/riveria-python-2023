# tee ratkaisu tänne
def viiva(pituus, merkkijono):
    if(merkkijono == ""):
        print("*"*pituus)
    else:
        print(merkkijono[0]*pituus)
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    viiva(5, "x")

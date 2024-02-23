# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(pituus, merkkijono):
    if(merkkijono == ""):
        print("*"*pituus)
    else:
        print(merkkijono[0]*pituus)

def risulaatikko(korkeus):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    iteraattori = 1
    while(iteraattori <= korkeus):
        viiva(10, "#")
        iteraattori += 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risulaatikko(5)

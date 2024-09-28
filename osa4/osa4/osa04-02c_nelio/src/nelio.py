# kopioi edellisestä tehtävästä funktion viiva koodi tänne
def viiva(pituus, merkkijono):
    if(merkkijono == ""):
        print("*"*pituus)
    else:
        print(merkkijono[0]*pituus)

def nelio(koko, merkki):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    iteraattori = 1
    while(iteraattori <= koko):
        viiva(koko, merkki)
        iteraattori += 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    nelio(5, "x")

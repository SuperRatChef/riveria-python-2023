# kopioi edellisestä tehtävästä funktion viiva koodi tänne, ja toteuta funktio kuvio sitä hyödyntäen
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
def viiva(pituus, merkkijono):
    if(merkkijono == ""):
        print("*"*pituus)
    else:
        print(merkkijono[0]*pituus)

def suorakulmio(korkeus, leveys, merkki):
    iteraattori = 1
    while(iteraattori <= korkeus):
        viiva(leveys, merkki)
        iteraattori += 1

def kolmio(koko, merkki):
    iteraattori = 1
    while(iteraattori <= koko):
        viiva(iteraattori, merkki)
        iteraattori += 1

def kuvio(kolmio_koko, kolmio_merkki, suorakulmio_koko, suorakulmio_korkeus):
    kolmio(kolmio_koko, kolmio_merkki)
    suorakulmio(suorakulmio_koko, kolmio_koko, suorakulmio_korkeus)
if __name__ == "__main__":
    kuvio(5, "x", 2, "o")

# tee ratkaisu tänne
def shakkilauta(koko):
    shakkinelio = "1"
    korkeus_iteraattori = 1
    rivi = ""
    while(korkeus_iteraattori <= koko):
        leveys_iteraattori = 1
        if(rivi != ""):
            shakkinelio = "1" if rivi[0] == "0" else "0"
        rivi = ""
        while(leveys_iteraattori <= koko):
            rivi += shakkinelio
            shakkinelio = "1" if shakkinelio == "0" else "0"
            leveys_iteraattori += 1
        print(rivi)
        korkeus_iteraattori += 1

# kokeillaan funktiota kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    shakkilauta(3)

# tee ratkaisu tänne
def suurin():
    with open("luvut.txt") as tiedosto:
        isoin = None

        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")
            #print(int(rivi))
            if(int(rivi) > (isoin or 0) or isoin == None):
                isoin = int(rivi)

        return isoin

if __name__ == "__main__":
    suurin = suurin()
    print(suurin)
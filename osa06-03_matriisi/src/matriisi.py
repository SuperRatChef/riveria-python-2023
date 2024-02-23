# tee ratkaisu tänne

def summa() -> int:
    summa = 0
    with open("matriisi.txt") as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")
            osat = rivi.split(",")
            for alkio in osat:
                summa += int(alkio)

    return summa


def maksimi():
    maksimi = None
    with open("matriisi.txt") as tiedosto:
        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")
            osat = rivi.split(",")
            for alkio in osat:
                if(int(alkio) > (maksimi or 0) or maksimi == None):
                    maksimi = int(alkio)
    return maksimi

def rivisummat() -> list:
    rivisummat = []
    with open("matriisi.txt") as tiedosto:
        for rivi in tiedosto:
            summa = 0
            rivi = rivi.replace("\n", "")
            osat = rivi.split(",")
            for alkio in osat:
                summa += int(alkio)
            rivisummat.append(summa)
    return rivisummat  

if __name__ == "__main__":
    summa = summa()
    print(summa)
    rivisummat = rivisummat()
    print(rivisummat)
    maksimi = maksimi()
    print(maksimi)
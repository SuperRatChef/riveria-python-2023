# tee ratkaisu tänne


def uusi_henkilo(nimi: str, ika: int) -> tuple:
    
    if(nimi == ""):
        raise ValueError("nimi on tyhjä merkkijono")
    if(len(nimi.split()) <= 1):
        raise ValueError("nimi ei koostu vähintään kahdesta sanasta")
    if(len(nimi) > 40):
        raise ValueError("nimen pituus on yli 40 merkkiä")
    if(ika < 0):
        raise ValueError("ikä on negatiivinen luku")
    if(150 < ika):
        raise ValueError("ikä on suurempi kuin 150")
    return (nimi, ika)

if __name__ == "__main__":
    nimi, ika = uusi_henkilo("aleksanteri kekkonen", 150)
    print(nimi, ika)


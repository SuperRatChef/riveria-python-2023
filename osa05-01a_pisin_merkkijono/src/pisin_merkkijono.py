# tee ratkaisu tänne

def pisin(mjonot: list):
    pisin_pituus = 0
    pisin = ""
    for mjono in mjonot:
        if(pisin_pituus < len(mjono)):
            pisin_pituus = len(mjono)
            pisin = mjono

    return pisin


if __name__ == "__main__":
    jonot = ["moi", "moikka", "heip", "hellurei", "terve"]
    print(pisin(jonot))

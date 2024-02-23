# tee ratkaisu tänne

def pisimman_pituus(lista):
    pisin = 0
    for sana in lista:
        if pisin < len(sana):
            pisin = len(sana)
    return pisin


if __name__ == "__main__":
    print(pisimman_pituus(["pekka", "emilia", "venla", "eero", "antti", "juhani"]))
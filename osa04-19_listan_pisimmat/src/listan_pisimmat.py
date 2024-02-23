# tee ratkaisu tänne
def pisimmat(lista):
    pisimmat = []
    pisin_pituus = None

    for sana in lista:
        if pisin_pituus == None or pisin_pituus == len(sana):
            pisin_pituus = len(sana)
            pisimmat.append(sana)
        elif pisin_pituus < len(sana):
            pisimmat = [sana]
            pisin_pituus = len(sana)
        else:
            continue
    return pisimmat

if __name__ == "__main__":
    print(pisimmat(["pekka", "emilia", "venla", "eero", "antti", "juhani"]))
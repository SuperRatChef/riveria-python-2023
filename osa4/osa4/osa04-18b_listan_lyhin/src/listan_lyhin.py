# tee ratkaisu tänne
def lyhin(lista):
    lyhin_pituus= 0
    lyhin_sana = None
    for sana in lista:
        if lyhin_pituus > len(sana) or lyhin_sana == None:
            lyhin_pituus = len(sana)
            lyhin_sana = sana
    return lyhin_sana


if __name__ == "__main__":
    print(lyhin(["pekka", "emilia", "venla", "eero", "antti", "juhani"]))
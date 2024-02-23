# tee ratkaisu tänne
def parilliset(lista):
    lista_parilliset = []
    for luku in lista:
        if luku % 2 == 0:
            lista_parilliset.append(luku)
    return lista_parilliset


if __name__ == "__main__":
    print(parilliset([1, 2, 3, 4, 5]))
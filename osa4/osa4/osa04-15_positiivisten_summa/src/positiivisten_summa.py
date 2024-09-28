# tee ratkaisu tänne
def positiivisten_summa(lista):
    summa = 0
    for luku in lista:
        if luku > 0:
            summa += luku

    return summa

if __name__ == "__main__":
    print(positiivisten_summa([1, -2, 3, -4, 5]))

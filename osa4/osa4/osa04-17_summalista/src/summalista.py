# tee ratkaisu tänne

def summa(lista1, lista2):
    summa_lista = []
    for i in range(len(lista1)):
        summa_lista.append(lista1[i]+lista2[i])

    return summa_lista

if __name__ == "__main__":
    print(summa([1, 2, 3], [7, 8, 9]))

# tee ratkaisu tänne
def laske_alkiot(matriisi: list, alkio: int):
    alkion_maara = 0
    for rivi in matriisi:
        for luku in rivi:
            if(luku == alkio):
                alkion_maara += 1
    return alkion_maara

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(laske_alkiot(m, 1))
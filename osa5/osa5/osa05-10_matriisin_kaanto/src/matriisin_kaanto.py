# tee ratkaisu tänne
def transponoi(matriisi: list):
    kopio = [rivi[:] for rivi in matriisi]
    
    for x in range(len(matriisi)):
        for y in range(len(matriisi)):
            kopio[x][y] = matriisi[y][x]
            
    matriisi[:] = kopio[:]

if __name__ == "__main__":
    matriisi = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    print(matriisi)
    transponoi(matriisi)
    print(matriisi)

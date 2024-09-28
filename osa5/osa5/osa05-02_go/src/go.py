# tee ratkaisu tänne
def kumpi_voitti(pelilauta: list):
    pelaaja1 = 0
    pelaaja2 = 0
    for rivi in pelilauta:
        for ruutu in rivi:
            if ruutu == 1:
                pelaaja1 += 1
            elif ruutu == 2:
                pelaaja2 += 1
    if(pelaaja1 < pelaaja2):
        return 2
    elif(pelaaja2 < pelaaja1):
        return 1
    else:
        return 0

if __name__ == "__main__":
    pelilauta = [[1, 2, 1],[0, 0, 1],[2, 1, 0]]
    print(kumpi_voitti(pelilauta))
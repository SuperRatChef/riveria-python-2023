# tee ratkaisu tänne
def kopioi_ja_lisaa(sudoku: list, rivi_nro: int, sarake_nro: int, luku: int):
    
    kopio = [rivi[:] for rivi in sudoku]

    for i in range(len(sudoku)):
        for j in range(len(sudoku)):
            kopio[i][j] = sudoku[i][j]
    
    kopio[rivi_nro][sarake_nro] = luku
    return kopio

def tulosta(sudoku):
    rivi_laskin = 0
    for rivi_sudoku in sudoku:
        tulostettava_rivi = []
        sarake_laskin = 1
        for ruutu in rivi_sudoku:
            if(ruutu == 0):
                tulostettava_rivi.append("_")
            else:
                tulostettava_rivi.append(str(ruutu))
            if(sarake_laskin % 3 == 0 and sarake_laskin % 9 != 0):
                tulostettava_rivi.append("")

            sarake_laskin += 1

        if(rivi_laskin % 3 == 0 and rivi_laskin % 9 != 0):
            print("")
        rivi_laskin += 1
        print(" ".join(tulostettava_rivi))


if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    kopio = kopioi_ja_lisaa(sudoku, 0, 0, 2)
    print("Alkuperäinen:")
    tulosta(sudoku)
    print()
    print("Kopio:")
    tulosta(kopio)
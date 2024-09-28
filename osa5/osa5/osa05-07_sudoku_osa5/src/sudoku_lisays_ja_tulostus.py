# tee ratkaisu tänne
def lisays(sudoku, rivi, sarake, alkio):
    sudoku[rivi][sarake] = alkio

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

    tulosta(sudoku)
    lisays(sudoku, 0, 0, 2)
    lisays(sudoku, 1, 2, 7)
    lisays(sudoku, 5, 7, 3)
    print()
    print("Kolme numeroa lisätty:")
    print()
    tulosta(sudoku)
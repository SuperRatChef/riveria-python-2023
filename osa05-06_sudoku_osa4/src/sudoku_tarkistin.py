# tee ratkaisu tänne

def nelio_oikein(sudoku: list, rivi_nro: int, sarake_nro: int):
    nelio = []
    for i in range(rivi_nro, rivi_nro+3):
        for j in range(sarake_nro, sarake_nro+3):
            nelio.append(sudoku[i][j])
    
    for i in range(1, 10):
        if(nelio.count(i) > 1):
            return False

    return True

def sarake_oikein(sudoku: list, sarake: int):
    sarake_rivi = []
    for i in range(len(sudoku)):
        sarake_rivi.append(sudoku[i][sarake])
    
    for i in range(1, 10):
        if(sarake_rivi.count(i) > 1):
            return False

    return True

def rivi_oikein(sudoku: list, rivi_nro: int):
    for i in range(1, 10):
        if(sudoku[rivi_nro].count(i) > 1):
            return False

    return True

def sudoku_oikein(sudoku: list):
    for rivi in range(0, 9):
        if(rivi_oikein(sudoku, rivi)):
            continue
        else: 
            return False
    
    for sarake in range(0, 9):
        if(sarake_oikein(sudoku, sarake)):
            continue
        else: 
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if(nelio_oikein(sudoku, i, j)):
                continue
            else:
                return False
    return True

if __name__ == "__main__":
    sudoku1 = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_oikein(sudoku1))

    sudoku2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_oikein(sudoku2))
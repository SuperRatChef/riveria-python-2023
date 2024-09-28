# tee ratkaisu tänne
def kertomat(n: int):
    kertomat = {}
    for i in range(1, n+1):
        kertoma = 1
        for j in range(1, i+1):
            kertoma *= j
        kertomat[i] = kertoma
    return kertomat
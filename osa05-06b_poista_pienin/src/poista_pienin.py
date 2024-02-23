# tee ratkaisu tänne
def poista_pienin(luvut):
    muokattu = []
    pienin = None
    for luku in luvut:
        if luku < int(pienin or 0) or pienin == None:
            pienin = luku

    for luku in luvut:
        if luku == pienin:
            continue
        else:
            muokattu.append(luku)
    
    luvut[:] = muokattu


if __name__ == "__main__":
    luvut = [2, 4, 6, 1, 3, 5]
    poista_pienin(luvut)
    print(luvut)
# tee ratkaisu tänne
def tee_tuple(x: int, y: int, z: int):
    pienin = min([x, y, z])
    suurin = max([x, y, z])
    summa = sum([x, y, z])
    return (pienin, suurin, summa)


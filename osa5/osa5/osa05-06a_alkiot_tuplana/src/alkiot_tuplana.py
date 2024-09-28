# tee ratkaisu tänne

def tuplaa_alkiot(luvut):
    tuplatut = []
    for luku in luvut:
        tuplatut.append(luku * 2)
    return tuplatut


if __name__ == "__main__":
    luvut = [2, 4, 5, 3, 11, -4]
    tuplaluvut = tuplaa_alkiot(luvut)
    print("alkuperäinen:", luvut)
    print("tuplattu:", tuplaluvut)
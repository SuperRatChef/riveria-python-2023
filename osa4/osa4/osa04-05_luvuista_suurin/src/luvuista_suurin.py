# tee ratkaisu tänne
def luvuista_suurin(a, b, c):
    arr = [a, b, c]
    arr.sort()
    return arr[2]
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti


if __name__ == "__main__":
    suurin = luvuista_suurin(5, 4, 8)
    print(suurin)
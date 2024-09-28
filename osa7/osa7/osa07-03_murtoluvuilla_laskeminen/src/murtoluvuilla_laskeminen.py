# tee ratkaisu tänne
from fractions import Fraction

def jaa_palasiksi(maara: int):
    palaset = []
    for i in range(maara):
        palaset.append(Fraction(f"{1}/{maara}"))
    return palaset

if __name__ == "__main__":
    print(jaa_palasiksi(5))
    
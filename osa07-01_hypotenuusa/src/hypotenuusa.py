# tee ratkaisu tänne
from math import sqrt

def hypotenuusa(kateetti1: float, kateetti2: float):
    return sqrt(kateetti1 ** 2 + kateetti2 ** 2)

if __name__ == "__main__":
    print(hypotenuusa(3, 4))

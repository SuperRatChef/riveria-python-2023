# tee ratkaisu tänne
import random
import string

def luo_salasana(pituus: int) -> str:
    salasana = ""

    salasanamerkit = ""

    for i in range(pituus):
        kirjain = random.choice(string.ascii_lowercase)
        salasana += kirjain

    return salasana

if __name__ == "__main__":
    for i in range(10):
        print(luo_salasana(8))
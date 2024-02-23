# tee ratkaisu tänne
import random
def heita(noppa: str):
    a = [3, 3, 3, 3, 3, 6]
    b = [2, 2, 2, 5, 5, 5]
    c = [1, 4, 4, 4, 4, 4]

    if(noppa == "A"): n = a
    if(noppa == "B"): n = b
    if(noppa == "C"): n = c

    return random.choice(n)
def pelaa(noppa1: str, noppa2: str, kertaa: int) -> tuple:
    noppa1_voitot = 0
    noppa2_voitot = 0
    tasapelit = 0

    for i in range(kertaa):
        n1 = heita(noppa1)
        n2 = heita(noppa2)

        if(n1 < n2):
            noppa2_voitot += 1
        elif(n1 > n2):
            noppa1_voitot += 1
        else:
            tasapelit += 1

    return noppa1_voitot, noppa2_voitot, tasapelit
    
if __name__ == "__main__":
    print(heita("A"))
    tulos = pelaa("A", "C", 1000)
    print(tulos)




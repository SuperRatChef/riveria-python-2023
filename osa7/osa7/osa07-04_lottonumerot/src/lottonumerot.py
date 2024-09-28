# tee ratkaisu tänne
from random import randint


def lottonumerot(maara: int, alaraja: int, ylaraja: int) -> list:
    lottonumerot = []
    while(len(lottonumerot) != maara):
        yritys = randint(alaraja, ylaraja+1)
        if(yritys not in lottonumerot):
            lottonumerot.append(yritys)
    return sorted(lottonumerot)

if __name__ == "__main__":
    lottonumerot = lottonumerot(7, 1, 40)
    print(lottonumerot)

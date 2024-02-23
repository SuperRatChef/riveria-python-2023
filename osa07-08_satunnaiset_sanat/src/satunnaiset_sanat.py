# tee ratkaisu tänne
import re
import random
def sanat(n: int, alku: str):
    sanat = []
    with open("sanat.txt") as tiedosto:
        for rivi in tiedosto:
            sanat.append(rivi.strip())

    hakutulokset = []
    for sana in sanat:
        if(re.match(f"^{alku}", sana) != None):
            hakutulokset.append(sana)
        else: 
            continue
        
    satunnaiset = []
    
    if(len(hakutulokset) < n):
        raise ValueError()
    else:
        while(True):
            satunnainen = random.choice(hakutulokset)
            if(satunnainen not in satunnaiset):
                satunnaiset.append(satunnainen)
            if(len(satunnaiset) == n):
                break
    
    return satunnaiset
        
if __name__ == "__main__":
    print(sanat(3, "ca"))
    

    
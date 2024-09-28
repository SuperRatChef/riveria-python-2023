# tee ratkaisu tänne
import re

def hae_sanat(hakusana: str):
    hakusana = f"^{hakusana.replace("*", ".*")}$"
    print(hakusana)

    tulokset = []

    with open("sanat.txt") as tiedosto:
        for rivi in tiedosto:
            sana = rivi.strip()
            if(re.search(hakusana, sana)):
                print(sana)
                tulokset.append(sana)

    return tulokset

if __name__ == "__main__":
    hae_sanat("*sh.sh")
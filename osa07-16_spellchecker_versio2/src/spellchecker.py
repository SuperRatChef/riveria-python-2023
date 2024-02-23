# tee ratkaisu tänne
from difflib import *

syote = input("write text: ")
syote_pilkottu = syote.split()
syote_korjattu = []

sanalista = []
with open("wordlist.txt") as tiedosto:
    for rivi in tiedosto:
        sanalista.append(rivi.strip())

korjausehdotukset = {}
for sana in syote_pilkottu:
    if(sana.lower() not in sanalista):
        syote_korjattu.append(f"*{sana}*")
        korjausehdotukset[sana] = get_close_matches(sana, sanalista)
    else:
        syote_korjattu.append(sana)

print(" ".join(syote_korjattu))
for korjausehdotus in korjausehdotukset.keys():
    print(f"{korjausehdotus}: {", ".join(korjausehdotukset[korjausehdotus])}")
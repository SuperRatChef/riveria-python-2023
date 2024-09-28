# tee ratkaisu tänne
#Hanki wordlista tiedostosta
wordlist = []
with open("wordlist.txt") as tiedosto:
    for word in tiedosto:
        wordlist.append(word.strip())
    
lause = input("Write text: ").split()

lause_korjattu = []
for sana in lause:
    if(sana.lower() not in wordlist):
        lause_korjattu.append(f"*{sana}*")
    else:
        lause_korjattu.append(sana)

print(" ".join(lause_korjattu))
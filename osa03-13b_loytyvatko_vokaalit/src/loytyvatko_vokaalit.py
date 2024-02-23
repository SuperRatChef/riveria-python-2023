# Kirjoita ratkaisu tähän

def etsi_kirjain(kirjain, merkkijono):
    for i in range(len(merkkijono)):
        #print(merkkijono[i])
        if(merkkijono[i] == kirjain):
            return True
    return False

merkkijono = input("Anna merkkijono: ")

if(etsi_kirjain("a", merkkijono)):
    print("a löytyy")
else:
    print("a ei löydy")

if(etsi_kirjain("e", merkkijono)):
    print("e löytyy")
else:
    print("e ei löydy")

if(etsi_kirjain("o", merkkijono)):
    print("o löytyy")
else:
    print("o ei löydy")
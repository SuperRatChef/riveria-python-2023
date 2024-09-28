# tee ratkaisu tänne

def hae_sanat(hakusana: str):
    hakusana = f"{hakusana.lower()}"
    #print(hakusana)

    tulokset = []

    with open("sanakirja.txt") as tiedosto:
        for rivi in tiedosto:
            sana = rivi.strip()
            if(hakusana in sana):
                tulokset.append(sana)

    return tulokset

def lisaa_sana(sana_suomeksi, sana_enlanniksi):
    with open("sanakirja.txt", "a") as tiedosto:
        tiedosto.write(f"{sana_suomeksi} - {sana_englanniksi}\n")


#with open("sanakirja.txt", "w") as tiedosto:
#    pass

print("1 - Lisää sana, 2 - Hae sanaa, 3 - Poistu")
valinta = int(input("Valinta: "))

while(valinta != 3):
    if(valinta == 1):
        sana_suomeksi = input("Anna sana suomeksi: ")
        sana_englanniksi = input("Anna sana englanniksi: ")
        lisaa_sana(sana_suomeksi, sana_englanniksi)
        print("Sanapari lisätty")
    elif(valinta == 2):
        hakusana = input("Anna sana: ")
        tulokset = hae_sanat(hakusana)
        [print(tulos) for tulos in tulokset]
    print("1 - Lisää sana, 2 - Hae sanaa, 3 - Poistu")
    valinta = int(input("Valinta: "))

print("Moi!")
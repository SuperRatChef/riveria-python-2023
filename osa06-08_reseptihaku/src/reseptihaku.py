# tee ratkaisu tänne


def lue_reseptit(tiedosto: str):
    reseptit = {}
    with open(tiedosto) as reseptikirja:
        resepti = []
        for rivi in reseptikirja:
            if(rivi.strip() != ""):
                resepti.append(rivi.strip())
            else:
                reseptit[resepti[0]] = resepti[1:]
                resepti = []
    reseptit[resepti[0]] = resepti[1:]
    resepti = []
    return reseptit

def hae_aika(tiedosto: str, aika: int):
    reseptit = lue_reseptit(tiedosto)
    hakutulokset = []
    for nimi, tiedot in reseptit.items():
        valmistusaika = int(tiedot[0])
        if(valmistusaika <= aika):
            hakutulokset.append(f"{nimi}, valmistusaika {valmistusaika} min")
        #print(valmistusaika)
    return hakutulokset

def hae_raakaaine(tiedosto: str, aine: str):
    reseptit = lue_reseptit(tiedosto)
    hakutulokset = []
    for nimi, tiedot in reseptit.items():
        valmistusaika = int(tiedot[0])
        raaka_aineet = tiedot[1:]
        for raaka_aine in raaka_aineet:
            if(raaka_aine.lower() in aine.lower()):
                hakutulokset.append(f"{nimi}, valmistusaika {valmistusaika} min")  
    return hakutulokset     

def hae_nimi(tiedosto: str, sana: str):
    reseptit = lue_reseptit(tiedosto)
    hakutulokset = []
    for resepti in reseptit.keys():
        if(sana.lower() in resepti.lower()):
            hakutulokset.append(resepti)
    return hakutulokset

if __name__ == "__main__":
    tulokset = hae_nimi("reseptit1.txt", "pulla")
    for resepti in tulokset:
        print(resepti)
    tulokset = hae_aika("reseptit1.txt", 20)
    for resepti in tulokset:
        print(resepti)
    tulokset = hae_raakaaine("reseptit1.txt", "maito")
    for resepti in tulokset:
        print(resepti)

# tee ratkaisu tänne
import csv 
from datetime import datetime, timedelta

def lue_aika(aika: str):
    tunnit = int(aika.split(":")[0])
    minuutit = int(aika.split(":")[1])
    return datetime(1, 1, 1, tunnit, minuutit, 0)
    
def viralliset_pisteet() -> dict:
    
    aloitusajat = {}
    with open("tentin_aloitus.csv") as tiedosto:
        for rivi in csv.reader(tiedosto, delimiter=";"):
            nimi = rivi[0]
            aloitusaika = rivi[1]
            aloitusajat[nimi] = lue_aika(aloitusaika)

    
    tehtavien_palautukset = {}
    with open("palautus.csv") as tiedosto:
        for rivi in csv.reader(tiedosto, delimiter=";"):
            nimi = rivi[0]
            tehtavanumero = rivi[1]
            pisteet = rivi[2]
            lopetusaika = lue_aika(rivi[3])
            
            if(nimi not in tehtavien_palautukset):
                tehtavien_palautukset[nimi] = []
            
            tehtavien_palautukset[nimi].append({
                "tehtavanumero": tehtavanumero,
                "pisteet": pisteet,
                "lopetusaika": lopetusaika
            })


    oppilaiden_oikeat_pisteet = {}

    for nimi in aloitusajat.keys():

        pistemaara = 0
        aikaraja = 180
        opiskelijan_palautukset = {}
        aloitusaika = aloitusajat[nimi]

        for palautus in tehtavien_palautukset[nimi]:

            tehtavanumero = palautus["tehtavanumero"]
            pisteet = palautus["pisteet"]
            lopetusaika = palautus["lopetusaika"]

            if(((lopetusaika - aloitusaika).total_seconds()/60) < aikaraja):
                if(tehtavanumero not in opiskelijan_palautukset):
                    opiskelijan_palautukset[tehtavanumero] = pisteet
                else:
                    if(opiskelijan_palautukset[tehtavanumero] < pisteet):
                        opiskelijan_palautukset[tehtavanumero] = pisteet
            else:
                pass
        print(nimi)
        pistemaara = sum([int(pisteet) for pisteet in opiskelijan_palautukset.values()])
        
        oppilaiden_oikeat_pisteet[nimi] = pistemaara

    return oppilaiden_oikeat_pisteet

if __name__ == "__main__":
    oppilaiden_pisteet = viralliset_pisteet()
    for nimi in oppilaiden_pisteet.keys():
        print(f"{nimi}: {oppilaiden_pisteet[nimi]}")
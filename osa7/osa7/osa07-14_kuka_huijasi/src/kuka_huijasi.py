# tee ratkaisu tänne
import csv 
from datetime import datetime, timezone

def luo_datetime(aika: str):
    tunnit = int(aika.split(":")[0].strip())
    minuutit = int(aika.split(":")[1].strip())
    return datetime(1, 1, 1, tunnit, minuutit, 0)

def huijarit():
    ajankohdat_aloitus = {}

    with open("tentin_aloitus.csv") as tiedosto:
        for rivi in tiedosto:
            nimi = rivi.split(";")[0].strip()
            aloitus = luo_datetime(rivi.split(";")[1].strip())
            ajankohdat_aloitus[nimi] = aloitus

    ajankohdat_lopetus = {}

    with open("palautus.csv") as tiedosto:
        for rivi in tiedosto:
            nimi = rivi.split(";")[0].strip()
            tehtava = rivi.split(";")[1].strip()
            pisteet = rivi.split(";")[2].strip()
            lopetus = luo_datetime(rivi.split(";")[3].strip())

            if(nimi in ajankohdat_lopetus and lopetus > ajankohdat_lopetus[nimi]):
                print("bigger time found")
                ajankohdat_lopetus[nimi] = lopetus
            elif(nimi not in ajankohdat_lopetus):
                print("adding")
                ajankohdat_lopetus[nimi] = lopetus
            print(lopetus, nimi)
            

    huijarit = []
    for nimi in ajankohdat_aloitus.keys():
        aloitus = ajankohdat_aloitus[nimi]
        lopetus = ajankohdat_lopetus[nimi]
        aikaero = lopetus - aloitus
        print("AikaEro ", aikaero.total_seconds() / 60)

        if(aikaero.total_seconds() / 60 > 180):
            huijarit.append(nimi)
    
    return huijarit
    
    
    

    
if __name__ == "__main__":
    date = luo_datetime("10:30")
    print(date)
    print(huijarit())
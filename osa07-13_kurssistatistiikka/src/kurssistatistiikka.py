# tee ratkaisu tänne
import urllib.request
import json


def hae_kaikki() -> list:

    #hae ja käsittele web pyyntö, hae kurssit verkosta kurssit muuttujaan
    kurssit_linkki = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    pyynto = urllib.request.urlopen(kurssit_linkki)
    kurssit_json =  pyynto.read().replace("'", '"')
    kurssit = json.loads(kurssit_json)
    
    #hae kaikki kurssit formatoituun muotoon, listaan johonka 
    #poimittu tupleja jotka sisältävät vain halutut tiedost kursseista
    kurssit_formatoitu = []
    for kurssi in kurssit:
        #hae vain kaikki meneillään olevat kurssit kurssit_formatoitu listaan
        if(kurssi["enabled"] == True):
            kurssin_kokonimi = kurssi["fullName"]
            kurssin_nimi = kurssi["name"]
            kurssin_vuosi = kurssi["year"]
            kurssin_harjoitusten_maara = sum(kurssi["exercises"])

            kurssit_formatoitu.append((kurssin_kokonimi, kurssin_nimi, kurssin_vuosi, kurssin_harjoitusten_maara))
    
    return kurssit_formatoitu

def hae_kurssi(kurssin_nimi: str) -> dict:
    #hae ja käsittele web pyynto, hae kurssi nimellä verkosta
    kurssin_linkki = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{kurssin_nimi}/stats"
    pyynto = urllib.request.urlopen(kurssin_linkki)
    kurssi_json = pyynto.read().replace("'", '"')
    kurssi = json.loads(kurssi_json)


    #hae kurssin olennaisimmat tiedot formatoituun muotoon
    kurssi_formatoitu = {}
    if(kurssi == {}):
        print("Annetulla nimellä ei löytynyt kursseja")
        return {}
    else:
        kurssi_formatoitu["viikkoja"] = len(kurssi.keys())
        kurssi_formatoitu["opiskelijoita"] = max([kurssi[i]["students"] for i in kurssi.keys()])
        kurssi_formatoitu["tunteja"] = sum([kurssi[i]["hour_total"] for i in kurssi.keys()])
        kurssi_formatoitu["tunteja_keskimaarin"] = int(kurssi_formatoitu["tunteja"]/kurssi_formatoitu["opiskelijoita"])
        kurssi_formatoitu["tehtavia"] = sum([kurssi[i]["exercise_total"] for i in kurssi.keys()])
        kurssi_formatoitu["tehtavia_keskimaarin"] = int(kurssi_formatoitu["tehtavia"]/kurssi_formatoitu["opiskelijoita"])


    return kurssi_formatoitu


if __name__ == "__main__":
    kurssit = hae_kaikki()
    for kurssi in kurssit:
        print(kurssi)
    kurssi = hae_kurssi("docker2019")
    print(kurssi)


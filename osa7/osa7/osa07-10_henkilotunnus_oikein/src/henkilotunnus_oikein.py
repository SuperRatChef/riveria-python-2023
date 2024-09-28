# tee ratkaisu tänne
from datetime import datetime, timedelta

def onko_validi(hetu: str) -> bool:
    paivamaara = int(hetu[0:2])
    kuukausi = int(hetu[2:4])
    vuosipart = int(hetu[4:6])
    valimerkki = hetu[6]
    vuosi = vuosipart
    yksilonumero = hetu[7:-1]
    tarkistemerkki = hetu[-1]
    tarkistusmerkkijono = "0123456789ABCDEFHJKLMNPRSTUVWXY"

    if(valimerkki == "+"): vuosi += 1800
    elif(valimerkki == "-"): vuosi += 1900
    elif(valimerkki == "A"): vuosi += 2000


    #tarkista paivamaaran oikeellisuus
    paivamaara_oikein = False
    try:
        syntymapaiva = datetime(vuosi, kuukausi, paivamaara)
        paivamaara_oikein = True
    except:
        pass
    

    #tarkista onko valimerkki oikea
    valimerkki_oikein = False
    if(valimerkki == "+"): valimerkki_oikein = True
    elif(valimerkki == "-"): valimerkki_oikein = True
    elif(valimerkki == "A"): valimerkki_oikein = True


    #tarkista tarkastusmerkin oikeellisuus
    tarkistemerkki_oikein = False
    try:
        numerosarja = int(hetu[0:6]+str(yksilonumero))
        tarkistemerkki_oikea = tarkistusmerkkijono[numerosarja%31]
        print(tarkistemerkki_oikea)
        print(tarkistemerkki)
        if(tarkistemerkki_oikea == tarkistemerkki):
            tarkistemerkki_oikein = True
    except: 
        pass
    
    #print(hetu, numerosarja, tarkistemerkki)

    if(paivamaara_oikein and valimerkki_oikein and tarkistemerkki_oikein):
        return True
    else:
        return False

    



if __name__ == "__main__":
    print(onko_validi("230827-906F1"))
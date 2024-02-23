import math

def hae_asematiedot(tiedosto: str) -> dict:
    asemat = {}
    with open(tiedosto) as tiedosto:
        for rivi in tiedosto:
            arvot = rivi.split(";")
            asema_nimi = arvot[3].strip()
            if(asema_nimi != "name"):
                longitude = float(arvot[0].strip())
                latitude = float(arvot[1].strip())
                asemat[asema_nimi] = (longitude, latitude)    
    return asemat


def etaisyys(asemat: dict, asema1: str, asema2: str) -> float:
    asema1_nimi = ""
    asema1_longitude = ""
    asema1_latitude = ""
    
    asema2_nimi = ""
    asema2_longitude = ""
    asema2_latitude = ""

    for nimi, etaisyydet in asemat.items():
        if(nimi.lower() == asema1.lower()):
            asema1_nimi = nimi
            asema1_longitude = etaisyydet[0]
            asema1_latitude = etaisyydet[1]
        if(nimi.lower() == asema2.lower()):
            asema2_nimi = nimi
            asema2_longitude = etaisyydet[0]
            asema2_latitude = etaisyydet[1]
    
    x_kilometreina = (asema1_longitude - asema2_longitude) * 55.26
    y_kilometreina = (asema1_latitude - asema2_latitude) * 111.2
    etaisyys = math.sqrt(x_kilometreina**2 + y_kilometreina**2)
    return etaisyys

def suurin_etaisyys(asemat: dict):
    asemanimet = asemat.keys()
    isoin_etaisyys = None
    asema1_nimi = None
    asema2_nimi = None
    for asema1 in asemanimet:
        for asema2 in asemanimet:
            pituus = etaisyys(asemat, asema1, asema2)
            print(pituus)
            if(isoin_etaisyys == None or pituus > float(isoin_etaisyys or 0)):
                isoin_etaisyys = pituus
                asema1_nimi = asema1
                asema2_nimi = asema2

    return (asema1_nimi, asema2_nimi, isoin_etaisyys)

if __name__ == "__main__":
    asemat = hae_asematiedot("stations1.csv")
    print(asemat)
    e = etaisyys(asemat, "Designmuseo", "Hietalahdentori")
    print(e)
    e = etaisyys(asemat, "Viiskulma", "Kaivopuisto")
    print(e)
    asemat = hae_asematiedot('stations1.csv')
    asema1, asema2, suurin = suurin_etaisyys(asemat)
    print(asema1, asema2, suurin)
# tee ratkaisu tänne
def tarkista_viikkonumero(rivi: str):
    viikko_nro = rivi.split(";")[0].split(" ")[1]
    if(int(viikko_nro)):
        print("oikea viikkonumero")
        return True
    else:
        raise ValueError()

def tarkista_numerotyyppi(rivi: str):
    numerot = [x.replace("\n", "") for x in rivi.split(";")[1].split(",")]
    numerot = [int(x) for x in numerot]
    print("numerot numeroita")
    return True

def tarkista_numeromaara(rivi: str):
    numerot = [x.replace("\n", "") for x in rivi.split(";")[1].split(",")]
    if(len(numerot) != 7):
        raise ValueError()
    print("oikea_maara_numeroita")
    return True

def tarkista_numerovali(rivi:str):
    numerot = [x.replace("\n", "") for x in rivi.split(";")[1].split(",")]
    numerot = [int(x) for x in numerot]
    for luku in numerot:
        if(1 <= int(luku) and int(luku <= 39)):
            continue
        else:
            raise ValueError()
    print("numerot rangella")
    return True

def onko_numero_kahdesti(rivi: str):
    numerot = [x.replace("\n", "") for x in rivi.split(";")[1].split(",")]
    numerot = [int(x) for x in numerot]
    numerot.sort()
    numerot_set = sorted(list(set(numerot)))
    print(numerot)
    print(numerot_set)
    if(numerot != numerot_set):
        raise ValueError()
    print("numeroa ei ole kahdesti")
    return True
    

def suodata_virheelliset():
    with open("korjatut_numerot.csv", "w") as korjatut:
        pass

    with open("lottonumerot.csv") as tiedosto:
        for rivi in tiedosto:
            try:
                viikko_oikein = tarkista_viikkonumero(rivi)
                numerot_numeroita = tarkista_numerotyyppi(rivi)
                oikeamaara_numeroita = tarkista_numeromaara(rivi)
                numerot_oikea_range = tarkista_numerovali(rivi)
                onko_sama_numero_kahdesti = onko_numero_kahdesti(rivi)
                

                print("oikein: ", rivi)
                with open("korjatut_numerot.csv", "a") as korjatut:
                    korjatut.write(f"{rivi}\n")
            except:
                print("väärin ", rivi)

if __name__ == "__main__":
    suodata_virheelliset()

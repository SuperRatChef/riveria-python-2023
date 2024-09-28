# tee ratkaisu tänne
def lisaa_opiskelija(opiskelijat: dict, opiskelija: str):
    opiskelijat[opiskelija] = {}

def lisaa_suoritus(opiskelijat: dict, opiskelija: str, suoritus: tuple):
    kurssin_nimi, arvosana = suoritus

    if(opiskelija in opiskelijat):
        if(0 < arvosana and arvosana <= 5):
            opiskelijan_kurssit = opiskelijat[opiskelija]
            if(kurssin_nimi in opiskelijan_kurssit):
                if(opiskelijan_kurssit[kurssin_nimi] < arvosana):
                    opiskelijan_kurssit[kurssin_nimi] = arvosana
            else:
                opiskelijan_kurssit[kurssin_nimi] = arvosana



    else:
        print("ei löytynyt ketään nimellä",opiskelija)
    
def tulosta(opiskelijat: dict, opiskelija: str):
    if(opiskelija in opiskelijat):
        print(f"{opiskelija}:")
        if(opiskelijat[opiskelija] == {}):
            print(" ei suorituksia")
        else:
            print(f" suorituksia {len(opiskelijat[opiskelija].keys())} kurssilta:")
            for (avain, arvo) in opiskelijat[opiskelija].items():
                print(f"  {avain} {arvo}")
            opiskelijan_keskiarvo = sum(opiskelijat[opiskelija].values())/len(opiskelijat[opiskelija].values())
            print(f" keskiarvo {opiskelijan_keskiarvo}")

    else:
        print("ei löytynyt ketään nimellä",opiskelija)

def kooste(opiskelijat: dict):
    opiskelijoiden_maara = len(opiskelijat.keys())
    eniten_suorituksia = 0
    eniten_suorituksia_opiskelija = ""
    paras_keskiarvo = 0
    paras_keskiarvo_opiskelija = ""

    
    for opiskelija in opiskelijat:
        opiskelijan_suoritukset = opiskelijat[opiskelija]
        keskiarvo = 0
        kurssien_maara = 0
        for kurssin_nimi, arvosana in opiskelijan_suoritukset.items():
            kurssien_maara += 1
            keskiarvo += arvosana
        keskiarvo = keskiarvo / len(opiskelijan_suoritukset.keys())

        if(keskiarvo > paras_keskiarvo):
            paras_keskiarvo = keskiarvo
            paras_keskiarvo_opiskelija = opiskelija
        if(kurssien_maara > eniten_suorituksia):
            eniten_suorituksia = kurssien_maara
            eniten_suorituksia_opiskelija = opiskelija


    print(f"opiskelijoita {opiskelijoiden_maara}")
    print(f"eniten suorituksia {eniten_suorituksia} {eniten_suorituksia_opiskelija}")
    print(f"paras keskiarvo {paras_keskiarvo} {paras_keskiarvo_opiskelija}")

if __name__ == "__main__":
    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "Pekka")
    lisaa_opiskelija(opiskelijat, "Liisa")
    lisaa_suoritus(opiskelijat, "Pekka", ("Lama", 1))
    lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 1))
    lisaa_suoritus(opiskelijat, "Pekka", ("Tira", 1))
    lisaa_suoritus(opiskelijat, "Liisa", ("Ohpe", 5))
    lisaa_suoritus(opiskelijat, "Liisa", ("Jtkt", 4))
    kooste(opiskelijat)
# tee ratkaisu tänne

def tulostatiedot(opiskelijatiedot, tehtavatiedot):
    opiskelijat = {}
    with open(opiskelijatiedot) as tiedosto:
        for rivi in tiedosto:
            osat = rivi.split(";")
            if(osat[0] == "opnro"):
                continue
            else:
                opnro = osat[0].strip()
                etunimi = osat[1].strip()
                sukunimi = osat[2].strip()
                opiskelijat[opnro] = {
                    "etunimi": etunimi,
                    "sukunimi": sukunimi
                }

    with open(tehtavatiedot) as tiedosto:
        for rivi in tiedosto:
            osat = rivi.split(";")
            if(osat[0] == "opnro"):
                continue
            else:
                opnro = osat[0].strip()
                opiskelijat[opnro]["tehtavat"] = [int(x.strip()) for x in osat[1:]]
    
    for opnro in opiskelijat:
        etunimi = opiskelijat[opnro]["etunimi"]
        sukunimi = opiskelijat[opnro]["sukunimi"]
        tehtavat = opiskelijat[opnro]["tehtavat"]
        print(f"{etunimi} {sukunimi} {sum(tehtavat)}")




opiskelijatiedot = input("Opiskelijatiedot: ")
tehtavatiedot = input("Tehtävätiedot: ")
tulostatiedot(opiskelijatiedot, tehtavatiedot)


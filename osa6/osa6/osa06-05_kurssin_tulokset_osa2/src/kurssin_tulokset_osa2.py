# tee ratkaisu tänne
# tee ratkaisu tänne

def tulostatiedot(opiskelijatiedot, tehtavatiedot, koepisteet):
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
    
    with open(koepisteet) as tiedosto:
        for rivi in tiedosto:
            osat = rivi.split(";")
            if(osat[0] == "opnro"):
                continue
            else:
                opnro = osat[0].strip()
                opiskelijat[opnro]["koepisteet"] = [int(x.strip()) for x in osat[1:]]

    for opnro in opiskelijat:
        koepisteet = sum(opiskelijat[opnro]["koepisteet"])
        tehtavamaara = sum(opiskelijat[opnro]["tehtavat"])
        tehtavapisteet = int((tehtavamaara / 40)*10)
        pisteet_yhteensa = koepisteet + tehtavapisteet
        arvosana = ""
        if(pisteet_yhteensa <= 14):
            arvosana = 0
        elif(15 <= pisteet_yhteensa and pisteet_yhteensa <= 17):
            arvosana = 1
        elif(18 <= pisteet_yhteensa and pisteet_yhteensa <= 20):
            arvosana = 2
        elif(21 <= pisteet_yhteensa and pisteet_yhteensa <= 23):
            arvosana = 3
        elif(24 <= pisteet_yhteensa and pisteet_yhteensa <= 27):
            arvosana = 4
        else:
            arvosana = 5
            
        opiskelijat[opnro]["arvosana"] = arvosana


    for opnro in opiskelijat:
        etunimi = opiskelijat[opnro]["etunimi"]
        sukunimi = opiskelijat[opnro]["sukunimi"]
        arvosana = opiskelijat[opnro]["arvosana"]
        print(f"{etunimi} {sukunimi} {arvosana}")




opiskelijatiedot = input("Opiskelijatiedot: ")
tehtavatiedot = input("Tehtävätiedot: ")
koepisteet = input("Koepisteet: ")
tulostatiedot(opiskelijatiedot, tehtavatiedot, koepisteet)


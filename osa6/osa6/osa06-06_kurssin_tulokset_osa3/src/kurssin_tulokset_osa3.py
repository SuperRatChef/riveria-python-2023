
def tulostatiedot(opiskelijatiedot, tehtavatiedot, koepisteet):
    #luo opiskelijat objekti, joka tallentaa itseensä tiedot opiskelijoista sekä heidän kurssisuorituksista
    opiskelijat = {}
    #lisää lista opiskelijoiden nimistä opiskelijat-kirjastoon
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
    #lisää lista suoritetuista tehtävämäärästä opiskelijat-kirjastoon
    with open(tehtavatiedot) as tiedosto:
        for rivi in tiedosto:
            osat = rivi.split(";")
            if(osat[0] == "opnro"):
                continue
            else:
                opnro = osat[0].strip()
                opiskelijat[opnro]["tehtavat"] = [int(x.strip()) for x in osat[1:]]
    
    #lisää lista koepisteistä opiskelijat-kirjastoon 
    with open(koepisteet) as tiedosto:
        for rivi in tiedosto:
            osat = rivi.split(";")
            if(osat[0] == "opnro"):
                continue
            else:
                opnro = osat[0].strip()
                opiskelijat[opnro]["koepisteet"] = [int(x.strip()) for x in osat[1:]]

    # laske ja lisaa arvosanat opiskelijoille koepisteiden ja tehtäväpisteiden mukaan opiskelijat-kirjastoon
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


    #tulosta tiedot opiskelijoista sekä heidän suorituksista opiskelijat-kirjastosta
    print(f"{"nimi":30}{"teht_lkm":10}{"teht_pist":10}{"koe_pist":10}{"yht_pist":10}{"arvosana":10}")
    for opnro in opiskelijat:
        tehtavamaara = sum(opiskelijat[opnro]["tehtavat"])
        etunimi = opiskelijat[opnro]["etunimi"]
        sukunimi = opiskelijat[opnro]["sukunimi"]
        tehtava_lkm = sum(opiskelijat[opnro]["tehtavat"])
        tehtavapisteet = int((tehtavamaara / 40)*10)
        koe_pisteet = sum(opiskelijat[opnro]["koepisteet"])
        yht_pisteet = tehtavapisteet + koe_pisteet
        arvosana = opiskelijat[opnro]["arvosana"]
        
        print(f"{etunimi+" "+sukunimi:30}{tehtava_lkm:<10}{tehtavapisteet:<10}{koe_pisteet:<10}{yht_pisteet:<10}{arvosana:<10}")




opiskelijatiedot = input("Opiskelijatiedot: ")
tehtavatiedot = input("Tehtävätiedot: ")
koepisteet = input("Koepisteet: ")
tulostatiedot(opiskelijatiedot, tehtavatiedot, koepisteet)


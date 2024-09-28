# Kirjoita ratkaisu tähän

def kysy_koepisteet_ja_harjoitukset():
    koepisteet = []
    harjoitukset = []

    syote = input("Koepisteet ja harjoitusten määrä: ")
    while(syote != ""):
        koepisteet.append(int(syote.split()[0]))
        harjoitukset.append(int(syote.split()[1]))
        syote = input("Koepisteet ja harjoitusten määrä: ")

    return (koepisteet, harjoitukset)

def laske_harjoituspisteet(harjoitukset):
    harjoituspisteet = []

    for harjoitus in harjoitukset:
        harjoituspisteet.append(harjoitus // 10)

    return harjoituspisteet

def laske_arvosanat(koepisteet, harjoituspisteet):
    arvosanat = []
    
    for kurssi in range(len(koepisteet)):
        tulos = koepisteet[kurssi] + harjoituspisteet[kurssi]
        if koepisteet[kurssi] < 10:
            arvosanat.append(0)
        else:
            if(0 <= tulos and tulos <= 14):
                arvosanat.append(0)
            if(15 <= tulos and tulos <= 17):
                arvosanat.append(1)
            if(18 <= tulos and tulos <= 20):
                arvosanat.append(2)
            if(21 <= tulos and tulos <= 23):
                arvosanat.append(3)
            if(24 <= tulos and tulos <= 27):
                arvosanat.append(4)
            if(28 <= tulos and tulos <= 30):
                arvosanat.append(5)
        
    return arvosanat

def tulosta_tilasto(koepisteet, harjoituspisteet, arvosanat):
    keskiarvo = (sum(koepisteet)+sum(harjoituspisteet))/len(koepisteet)
    hyväksymisprosentti = len(list(filter(lambda x: (x != 0), arvosanat)))/len(arvosanat)*100
    print("Tilasto: ")
    print(f"Pisteiden keskiarvo: {keskiarvo:.1f}")
    print(f"Hyväksymisprosentti: {hyväksymisprosentti:.1f}")
    print("Arvosanajakauma:")
    print("  5:","*"*arvosanat.count(5))
    print("  4:","*"*arvosanat.count(4))
    print("  3:","*"*arvosanat.count(3))
    print("  2:","*"*arvosanat.count(2))
    print("  1:","*"*arvosanat.count(1))
    print("  0:","*"*arvosanat.count(0))




(koepisteet, harjoitukset) = kysy_koepisteet_ja_harjoitukset()
harjoituspisteet = laske_harjoituspisteet(harjoitukset)
arvosanat = laske_arvosanat(koepisteet, harjoituspisteet)
#print(koepisteet)
#print(harjoitukset)
#print(harjoituspisteet)
#print(arvosanat)
tulosta_tilasto(koepisteet, harjoituspisteet, arvosanat)

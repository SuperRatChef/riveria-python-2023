# Kirjoita ratkaisu tähän

def kirjainRuudukko(kerrokset: int):
    for i in range(kerrokset*2-1):
        rivi = ""
        for j in range(kerrokset*2-1):
            etaisyys_keskikohdasta_korkeus = abs(kerrokset-1 - i)
            etaisyys_keskikohdasta_leveys = abs(kerrokset-1 - j)
            #print(etaisyys_keskikohdasta_korkeus)
            #print(etaisyys_keskikohdasta_leveys)
            etaisyys_keskikohdasta = max([etaisyys_keskikohdasta_korkeus, etaisyys_keskikohdasta_leveys])
            kirjain = chr(ord("A")+(etaisyys_keskikohdasta))
            rivi += kirjain
        print(rivi)
            

kerrokset = int(input("Kerrokset: "))
kirjainRuudukko(kerrokset)
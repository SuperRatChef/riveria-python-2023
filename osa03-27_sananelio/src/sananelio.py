# tee ratkaisu tänne
def nelio(merkkijono, koko):
    kirjain_iteraattori = 0
    ruutu = merkkijono[kirjain_iteraattori]
    korkeus_iteraattori = 1
    
    while(korkeus_iteraattori <= koko):
        rivi = ""
        leveys_iteraattori = 1
        while(leveys_iteraattori <= koko):
            rivi += ruutu
            kirjain_iteraattori += 1
            ruutu = merkkijono[kirjain_iteraattori % len(merkkijono)]
            leveys_iteraattori += 1
            
        print(rivi)
        korkeus_iteraattori += 1

if __name__ == "__main__":
    nelio("abcd", 5)
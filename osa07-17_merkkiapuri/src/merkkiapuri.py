# tee ratkaisu tänne
import string

def vaihda_koko(merkkijono: str) -> str:
    koko_vaihdettu = ""
    for merkki in merkkijono:
        if(merkki.islower()):
            koko_vaihdettu += merkki.upper()
        else:
            koko_vaihdettu += merkki.lower()
    return koko_vaihdettu

def puolita(merkkijono: str) -> tuple:
    eka_osa = merkkijono[:int(len(merkkijono)/2)]
    toka_osa = merkkijono[int(len(merkkijono)/2):]
    return eka_osa, toka_osa

def poista_erikoismerkit(merkkijono: str):
    merkkijono_erikoismerkit_poistettu = ""
    kirjaimet = string.ascii_letters+"äöÄÖ"+string.digits+" "

    for kirjain in merkkijono:
        if(kirjain in kirjaimet):
            merkkijono_erikoismerkit_poistettu += kirjain
        
    return merkkijono_erikoismerkit_poistettu
        

if __name__ == "__main__":
    mjono = "Moi kaikki!"

    print(vaihda_koko(mjono))

    p1, p2 = puolita(mjono)

    print(p1)
    print(p2)

    m2 = poista_erikoismerkit("Tämä on testi, katsotaan miten käy!!!11!")
    print(m2)
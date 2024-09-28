# tee ratkaisu tänne
import string

def jaa_merkkeihin(merkkijono: str):
    pienet_ja_suuret = []
    punctuation = []
    misc = []
    for kirjain in merkkijono:
        if(kirjain in string.ascii_letters):
            pienet_ja_suuret.append(kirjain)
        elif(kirjain in string.punctuation):
            punctuation.append(kirjain)
        else:
            misc.append(kirjain)

    return "".join(pienet_ja_suuret), "".join(punctuation), "".join(misc)

if __name__ == "__main__":
    osat = jaa_merkkeihin("Tämä on testi!!! Toimiiko, mitä?")
    print(osat[0])
    print(osat[1])
    print(osat[2])
            
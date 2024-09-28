# tee ratkaisu tänne

def kaanna(sanakirja: dict):
    kaannetty = {}
    for avain, arvo in sanakirja.items():
        kaannetty[arvo] = avain

    for avain, arvo in kaannetty.items():
        del sanakirja[arvo]

    for avain, arvo in kaannetty.items():
        sanakirja[avain] = arvo

if __name__ == "__main__":
    s = {1: "eka", 2: "toka", 3: "kolmas", 4: "neljas"}
    kaanna(s)
    print(s)
# tee ratkaisu tänne

def vanhin(henkilot: list):
    vanhin = ""
    vanhin_syntymavuosi = 2024
    for (nimi, syntymavuosi) in henkilot:
        if(syntymavuosi < vanhin_syntymavuosi):
            vanhin = nimi
            vanhin_syntymavuosi = syntymavuosi
    return vanhin

if __name__ == "__main__":
    h1 = ("Arto", 1977)
    h2 = ("Einari", 1985)
    h3 = ("Maija", 1953)
    h4 = ("Essi", 1997)
    hlista = [h1, h2, h3, h4]

    print(vanhin(hlista))
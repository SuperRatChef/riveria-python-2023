# tee ratkaisu tänne

def tallenna_henkilo(henkilo: tuple):
    nimi, ika, pituus = henkilo
    with open("henkilot.csv", "a") as tiedosto:
        tiedosto.write(f"{nimi};{ika};{pituus}\n")
    

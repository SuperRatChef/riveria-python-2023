# tee ratkaisu tänne
nimi = input("Kenelle teos omistetaan: ")
tiedosto_nimi = input("Mihn kirjoitetaan: ")

with open(tiedosto_nimi, "w") as tiedosto:
    tiedosto.write(f"Hei {nimi}, toivomme viihtyisiä hetkiä python-kurssimateriaalin parissa! Terveisin mooc.fi-tiimi")
# tee ratkaisu tänne,
from datetime import datetime, timedelta

tiedosto_nimi = input("Tiedosto: ")

aloitus_input = input("Aloituspäivä: ")
paiva = int(aloitus_input.split(".")[0])
kuukausi = int(aloitus_input.split(".")[1])
vuosi = int(aloitus_input.split(".")[2])
aloituspaivamaara = datetime(vuosi, kuukausi, paiva)

montako_paivaa = int(input("Montako päivää: "))
lopetuspaivamaara = aloituspaivamaara+timedelta(days=montako_paivaa-1)
print("Anna ruutuajat kunakin päivänä minuutteina (TV tietokone mobiililaite):")

ruutuajat = []
yht_minuutteja = 0
ruutuajat_summat = []
for i in range(montako_paivaa):
    ruutuaika = input("Ruutuaika: ")
    tv = int(ruutuaika.split()[0])
    tietokone = int(ruutuaika.split()[1])
    mobiili = int(ruutuaika.split()[2])
    ruutuajat.append((tv, tietokone, mobiili))
    yht_minuutteja += tv + tietokone + mobiili
    ruutuajat_summat.append(tv + tietokone + mobiili)

keskimaarin_minuutteja = sum(ruutuajat_summat)/len(ruutuajat_summat)


with open(tiedosto_nimi, "w") as tiedosto:
    tiedosto.write(f"Ajanjakso: {aloituspaivamaara.strftime("%d.%m.%Y")}-{lopetuspaivamaara.strftime("%d.%m.%Y")}\n")
    tiedosto.write(f"Yht. minuutteja: {yht_minuutteja}\n")
    tiedosto.write(f"Keskim. minuutteja: {keskimaarin_minuutteja}\n")
    for i in range(montako_paivaa):
        paivamaara = aloituspaivamaara+timedelta(days=i)
        tiedosto.write(f"{paivamaara.strftime("%d.%m.%Y")}: {"/".join([str(x) for x in ruutuajat[i]])}\n")
print(yht_minuutteja, ruutuajat, keskimaarin_minuutteja)

# tee ratkaisu tänne
from datetime import datetime

paiva = int(input("Päivä: "))
kuukausi = int(input("Kuukausi: "))
vuosi = int(input("Vuosi: "))

henkilon_syntymahetki = datetime(vuosi, kuukausi, paiva)
paivamaara = datetime(1999, 12, 31)

paivaa_vanha = (paivamaara-henkilon_syntymahetki).days

if(paivaa_vanha < 0):
    print("Et ollut syntynyt, kun vuosituhat vaihtui")
else:
    print(f"Olit {paivaa_vanha} päivää vanha, kun vuosituhat vaihtui")
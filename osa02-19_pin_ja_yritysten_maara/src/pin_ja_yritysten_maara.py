# Kirjoita ratkaisu tähän

yritysten_maara = 1
pin = 4321
pin_arvaus = int(input("PIN-koodi: ")) 

while(pin != pin_arvaus):
    print("Väärin")
    pin_arvaus = int(input("PIN-koodi: ")) 
    yritysten_maara += 1

if(yritysten_maara == 1):
    print("Oikein, tarvitsit vain yhden yrityksen!")
else:
    print(f"Oikein, tarvitsit {yritysten_maara} yritystä")


# Kirjoita ratkaisu tähän
tuntipalkka = float(input("tuntipalkka: "))
tyotunnit = int(input("Työtunnit"))
viikonpaiva = input("Viikonpäivä")
palkka = 0

if(viikonpaiva == "sunnuntai"):
    palkka = tuntipalkka * tyotunnit * 2
else:
    palkka = tuntipalkka * tyotunnit
print("Palkka", palkka, "euroa")   
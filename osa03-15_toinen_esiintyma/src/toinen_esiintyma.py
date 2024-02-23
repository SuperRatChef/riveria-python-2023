# Kirjoita ratkaisu tähän

merkkijono = input("Anna merkkijono: ")
osajono = input("Anna osajono: ")
eka_esiintyma = merkkijono.find(osajono)
toinen_esiintyma = -1 

if(eka_esiintyma != -1):
    merkkijono_patka = merkkijono[eka_esiintyma+len(osajono):]
    toinen_esiintyma = merkkijono_patka.find(osajono)
    if(toinen_esiintyma != -1):
        toinen_esiintyma += len(merkkijono)-len(merkkijono_patka)

if(toinen_esiintyma == -1):
    print("Osajono ei esiinny merkkijonossa kahdesti.")
else:
    print(f"Osajonon toinen esiintymä on kohdassa {toinen_esiintyma}.")
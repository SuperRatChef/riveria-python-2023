# Kirjoita ratkaisu tähän

ika = int(input("Kerro ikäsi? "))

if(ika < 5):
    if(ika < 0):
        print("Taitaa olla virhe")
    else:
        print("En usko, että osaat kirjoittaa")
else:
    print(f"Ok, olet siis {ika}-vuotias")
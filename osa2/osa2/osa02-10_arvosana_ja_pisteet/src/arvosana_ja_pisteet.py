# Kirjoita ratkaisu tähän
arvosana = int(input("Anna pisteet [0-100]: "))

tulos = ""

if(arvosana < 0):
    tulos = "mahdotonta!"
elif(0 <= arvosana and arvosana <= 49):
    tulos = "hylätty"
elif(50 <= arvosana and arvosana <= 59):
    tulos = "1"
elif(60 <= arvosana and arvosana <= 69):
    tulos = "2"
elif(70 <= arvosana and arvosana <= 79):
    tulos = "3"
elif(80 <= arvosana and arvosana <= 89):
    tulos = "4"
elif(90 <= arvosana and arvosana <= 100):
    tulos = "5"
else:
    tulos = "mahdotonta!"


print(f"Arvosana: {tulos}")
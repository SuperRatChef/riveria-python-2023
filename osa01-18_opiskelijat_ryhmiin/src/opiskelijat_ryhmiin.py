# Kirjoita ratkaisu tähän
opiskelijoiden_maara = int(input("Montako opiskelijaa?"))
ryhmakoko = int(input("Mikä on ryhmän koko?"))
ryhmien_maara = 0
if(opiskelijoiden_maara % ryhmakoko == 0):
    ryhmien_maara = opiskelijoiden_maara / ryhmakoko
else:
    ryhmien_maara = opiskelijoiden_maara // ryhmakoko + 1
print("Ryhmien määrä:", ryhmien_maara)
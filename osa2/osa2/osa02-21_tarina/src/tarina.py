# Kirjoita ratkaisu tähän
tarina = []
sana = input("Anna sana: ")
while(sana != "loppu"):
    tarina.append(sana)
    yritys = input("Anna sana: ")
    if(yritys == sana):
        sana = "loppu"
    else:
        sana = yritys
print(" ".join(tarina))
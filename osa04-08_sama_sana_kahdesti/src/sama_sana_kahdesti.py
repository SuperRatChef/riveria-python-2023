# Kirjoita ratkaisu tähän
sanoja = []
while(True):
    sana = input("sana: ")
    if sana in sanoja:
        break
    else:
        sanoja.append(sana)
print(f"Annoit {len(sanoja)} eri sanaa")
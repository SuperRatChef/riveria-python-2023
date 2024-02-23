# Kirjoita ratkaisu tähän
def onkoKarkausvuosi(vuosi):
    onko_karkausvuosi = False
    if(vuosi % 4 == 0):
        if(vuosi % 100 == 0):
            if(vuosi % 400 == 0):
                onko_karkausvuosi = True
            else:
                onko_karkausvuosi = False
        else:
            onko_karkausvuosi = True
    else:
        onko_karkausvuosi = False
    
    return onko_karkausvuosi


vuosi = int(input("Vuosi: "))

seuraava_karkausvuosi = vuosi+1

while(not onkoKarkausvuosi(seuraava_karkausvuosi)):
    seuraava_karkausvuosi = seuraava_karkausvuosi+1

print(f"Vuotta {vuosi} seuraava karkausvuosi on {seuraava_karkausvuosi}")
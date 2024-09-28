# Kirjoita ratkaisu tähän

vuosi = int(input("Anna vuosi: "))
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

if(onko_karkausvuosi):
    print("Vuosi on karkausvuosi")
else:
    print("Vuosi ei ole karkausvuosi")
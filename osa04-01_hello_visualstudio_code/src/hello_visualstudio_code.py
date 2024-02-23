# Kirjoita ratkaisu tähän
editori = ""
while(editori != "visual studio code"):
    editori = input("Editori: ").lower()
    if(editori == "word" or editori == "notepad"):
        print("surkea")
    elif(editori == "visual studio code"):
        print("loistava valinta!")
    else:
        print("ei ole hyvä")
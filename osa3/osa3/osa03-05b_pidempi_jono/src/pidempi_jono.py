# Kirjoita ratkaisu tähän
merkkijono1 = input("Anna jono 1: ")
merkkijono2 = input("Anna jono 2: ")

if(len(merkkijono1) < len(merkkijono2)):
    print(f"{merkkijono2} on pidempi")
elif(len(merkkijono2) < len(merkkijono1)):
    print(f"{merkkijono1} on pidempi")
else:
    print("Jonot ovat yhtä pitkät")
    
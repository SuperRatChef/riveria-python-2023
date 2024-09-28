# tee ratkaisu tänne
import string

def suorita(ohjelma: list):
    muuttujat = {x: 0 for x in string.ascii_uppercase}
    tulostus = []
    ohjelma_counter = 0
    #print(muuttujat)

    while(ohjelma_counter < len(ohjelma) and (ohjelma[ohjelma_counter] != "END" or True)):

        operaatio = ohjelma[ohjelma_counter]
        komento = operaatio.split()[0]


        #print(ohjelma[ohjelma_counter])

        if(komento == "PRINT"):
            kohde = operaatio.split()[1]
            if(kohde in muuttujat):
                tulostus.append(muuttujat[kohde])
            else:
                tulostus.append(int(kohde))

        if(komento == "MOV"):
            kohde = operaatio.split()[1]
            arvo = operaatio.split()[2]
            if(arvo in muuttujat.keys()):
                muuttujat[kohde] = muuttujat[arvo] 
            else:
                muuttujat[kohde] = int(arvo)

        if(komento == "ADD"):
            kohde = operaatio.split()[1]
            arvo = operaatio.split()[2]
            if(arvo in muuttujat.keys()):
                muuttujat[kohde] += muuttujat[arvo] 
            else:
                muuttujat[kohde] += int(arvo)
                
        if(komento == "SUB"):
            kohde = operaatio.split()[1]
            arvo = operaatio.split()[2]
            if(arvo in muuttujat.keys()):
                muuttujat[kohde] -= muuttujat[arvo] 
            else:
                muuttujat[kohde] -= int(arvo)

        if(komento == "MUL"):
            kohde = operaatio.split()[1]
            arvo = operaatio.split()[2]
            if(arvo in muuttujat.keys()):
                muuttujat[kohde] *= muuttujat[arvo] 
            else:
                muuttujat[kohde] *= int(arvo)

        if(komento == "JUMP"):
            kohde = operaatio.split()[1]
            ohjelma_counter = ohjelma.index(f"{kohde}:")

        if(komento == "IF"):
            ehto_parametri_a = operaatio.split()[1]
            ehto = operaatio.split()[2]
            ehto_parametri_b = operaatio.split()[3]
            kohde = operaatio.split()[5]
            #print(kohde)

            if(ehto_parametri_a in muuttujat.keys()):
                ehto_parametri_a = str(muuttujat[ehto_parametri_a])
            else:
                pass

            if(ehto_parametri_b in muuttujat.keys()):
                ehto_parametri_b = str(muuttujat[ehto_parametri_b])
            else:
                pass

            if(eval("".join([ehto_parametri_a, ehto, ehto_parametri_b]))):
                ohjelma_counter = ohjelma.index(f"{kohde}:")
                #print(ohjelma_counter)
            else:
                #print(muuttujat)
                #print("ehto ei täyty")
                pass
            #print(ehto)
            #print(ohjelma[ohjelma_counter])


        
        ohjelma_counter += 1

        
    

    return tulostus
    

if __name__ == "__main__":
    ohjelma1 = []
    ohjelma1.append("MOV A 1")
    ohjelma1.append("MOV B 2")
    ohjelma1.append("PRINT A")
    ohjelma1.append("PRINT B")
    ohjelma1.append("ADD A B")
    ohjelma1.append("PRINT A")
    ohjelma1.append("END")
    tulos = suorita(ohjelma1)
    print(tulos)

    ohjelma2 = []
    ohjelma2.append("MOV A 1")
    ohjelma2.append("MOV B 10")
    ohjelma2.append("alku:")
    ohjelma2.append("IF A >= B JUMP loppu")
    ohjelma2.append("PRINT A")
    ohjelma2.append("PRINT B")
    ohjelma2.append("ADD A 1")
    ohjelma2.append("SUB B 1")
    ohjelma2.append("JUMP alku")
    ohjelma2.append("loppu:")
    ohjelma2.append("END")
    tulos = suorita(ohjelma2)
    print(tulos)

    ohjelma3 = []
    ohjelma3.append("MOV A 1")
    ohjelma3.append("MOV B 1")
    ohjelma3.append("alku:")
    ohjelma3.append("PRINT A")
    ohjelma3.append("ADD B 1")
    ohjelma3.append("MUL A B")
    ohjelma3.append("IF B <= 10 JUMP alku")
    ohjelma3.append("END")
    tulos = suorita(ohjelma3)
    print(tulos)

    ohjelma4 = []
    ohjelma4.append("MOV N 50")
    ohjelma4.append("PRINT 2")
    ohjelma4.append("MOV A 3")
    ohjelma4.append("alku:")
    ohjelma4.append("MOV B 2")
    ohjelma4.append("MOV Z 0")
    ohjelma4.append("testi:")
    ohjelma4.append("MOV C B")
    ohjelma4.append("uusi:")
    ohjelma4.append("IF C == A JUMP virhe")
    ohjelma4.append("IF C > A JUMP ohi")
    ohjelma4.append("ADD C B")
    ohjelma4.append("JUMP uusi")
    ohjelma4.append("virhe:")
    ohjelma4.append("MOV Z 1")
    ohjelma4.append("JUMP ohi2")
    ohjelma4.append("ohi:")
    ohjelma4.append("ADD B 1")
    ohjelma4.append("IF B < A JUMP testi")
    ohjelma4.append("ohi2:")
    ohjelma4.append("IF Z == 1 JUMP ohi3")
    ohjelma4.append("PRINT A")
    ohjelma4.append("ohi3:")
    ohjelma4.append("ADD A 1")
    ohjelma4.append("IF A <= N JUMP alku")
    tulos = suorita(ohjelma4)
    print(tulos)
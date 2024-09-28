# tee ratkaisu tänne
import random
import string

def luo_hyva_salasana(pituus: int, onko_numeroita: bool, onko_erikoismerkkeja: bool) -> str:
    salasana = ""    

    salasanamerkit = string.ascii_lowercase
    if(onko_numeroita): salasanamerkit += string.digits
    if(onko_erikoismerkkeja): salasanamerkit += "!?=+-()#"

    while(True):
        salasana = ""

        for i in range(pituus):
            kirjain = random.choice(salasanamerkit)
            salasana = salasana + kirjain
            print(salasana)
        print("exiting loop")

        tayttyyko_aakkoset = False
        tayttyyko_numerot = False
        tayttyyko_erikoismerkit = False

        if(True):
            for kirjain in salasana:
                if kirjain in string.ascii_lowercase:
                    tayttyyko_aakkoset = True

        if(onko_numeroita):
            for kirjain in salasana:
                if kirjain in string.digits:
                    tayttyyko_numerot = True
        else:
            tayttyyko_numerot = True

        if(onko_erikoismerkkeja):
            for kirjain in salasana:
                if kirjain in "!?=+-()#":
                    tayttyyko_erikoismerkit = True
        else:
            tayttyyko_erikoismerkit = True

        print(f"tayttyyko isalpha", tayttyyko_aakkoset)
        print(f"tayttyyko numerot", tayttyyko_numerot)
        print(f"tayttyyko erikois", tayttyyko_erikoismerkit)
        if(tayttyyko_aakkoset and tayttyyko_numerot and tayttyyko_erikoismerkit):
            break

        

    return salasana

if __name__ == "__main__":
    for i in range(10):
        print(luo_hyva_salasana(5, True, False))
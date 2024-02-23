# tee ratkaisu tänne
def joulukuusi(koko):
    print("joulukuusi!")
    iteraattori = 1
    while(iteraattori <= koko):
        tyhjäsivu = " "*((koko-iteraattori))
        rivi = tyhjäsivu+("*"*(iteraattori*2-1))+tyhjäsivu
        print(rivi)
        iteraattori += 1
    tyhjäsivu = " "*(koko-1)
    rivi =  tyhjäsivu+"*"+tyhjäsivu
    print(rivi)
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    joulukuusi(3)
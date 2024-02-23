# tee ratkaisu tänne
def samat(sana, indeksi1, indeksi2):
    if(indeksi1 >= len(sana) or indeksi2 >= len(sana)):
        return False
    if(sana[indeksi1] == sana[indeksi2]):
        return True
    else:
        return False
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    print(samat("koodari", 1, 10)) 
    
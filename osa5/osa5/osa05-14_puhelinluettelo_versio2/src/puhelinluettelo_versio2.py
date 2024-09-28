# tee ratkaisu tänne


def hae_numero(puhelinLuettelo: dict, nimi: str):
    if nimi not in puhelinLuettelo:
        print("ei numeroa")
    else:
        if(len(puhelinLuettelo[nimi]) == 1):
            print(*puhelinLuettelo[nimi])
        else:
            print(*puhelinLuettelo[nimi], sep = "\n")

def lisaa(puhelinLuettelo: dict):
    nimi = input("nimi: ")
    numero = input("numero: ")
    
    if(nimi not in puhelinLuettelo):
        puhelinLuettelo[nimi] = []
        puhelinLuettelo[nimi].append(numero)
    else:
        puhelinLuettelo[nimi].append(numero)
    print("ok!")


puhelinLuettelo = {}
komento = int(input("komento (1 hae, 2 lisää, 3 lopeta): "))
while(komento != 3):
    if(komento == 1):
        nimi = input("nimi: ")
        hae_numero(puhelinLuettelo, nimi)
    elif(komento == 2):
        lisaa(puhelinLuettelo)
    
    komento = int(input("komento (1 hae, 2 lisää, 3 lopeta): "))
    
print("lopetetaan...")
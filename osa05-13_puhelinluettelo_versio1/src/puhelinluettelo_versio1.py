# tee ratkaisu tänne

def hae_numero(puhelinLuettelo: dict, nimi: str) -> str:
    if nimi not in puhelinLuettelo:
        return "ei numeroa"
    else:
        return puhelinLuettelo[nimi]

def lisaa(puhelinLuettelo: dict):
    nimi = input("nimi: ")
    numero = input("numero: ")
    puhelinLuettelo[nimi] = numero
    print("ok!")


puhelinLuettelo = {}
komento = int(input("komento (1 hae, 2 lisää, 3 lopeta): "))
while(komento != 3):
    if(komento == 1):
        nimi = input("nimi: ")
        print(hae_numero(puhelinLuettelo, nimi))
    elif(komento == 2):
        lisaa(puhelinLuettelo)
    
    komento = int(input("komento (1 hae, 2 lisää, 3 lopeta): "))
    
print("lopetetaan...")
# tee ratkaisu tänne
def kaikki_vaarinpain(lista: list):
    vaarinpain = []
    for sana in lista:
        vaarinpain.append(sana[::-1])
    return vaarinpain[::-1]

if __name__ == "__main__":
    lista = ["Moi", "kaikki", "esimerkki", "vielä yksi"]
    print(kaikki_vaarinpain(lista))
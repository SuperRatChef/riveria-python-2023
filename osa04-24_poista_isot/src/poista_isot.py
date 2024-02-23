# tee ratkaisu tänne

def poista_isot(lista: list):
    lista_pienet = []
    for sana in lista:
        if(sana.isupper()):
            continue
        else:
            lista_pienet.append(sana)
    return lista_pienet

    
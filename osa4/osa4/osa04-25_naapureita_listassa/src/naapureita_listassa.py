# tee ratkaisu tänne
def pisin_naapurijono(luvut: list):
    pisin_naapurijono = 0
    nykyinen_naapurijono = 0
    edellinen_luku = None
    
    for nykyinen_luku in luvut:
        if edellinen_luku == None:
            nykyinen_naapurijono = 1
            edellinen_luku = nykyinen_luku
            continue
        else:
            lukuero = abs(nykyinen_luku - edellinen_luku)
            #print(lukuero)
            if(lukuero == 1):
                nykyinen_naapurijono += 1
            else:
                nykyinen_naapurijono = 1
        
            if(nykyinen_naapurijono > pisin_naapurijono):
                pisin_naapurijono = nykyinen_naapurijono

            edellinen_luku = nykyinen_luku
            #print("Nykyinen naapurijono", nykyinen_naapurijono)
    return pisin_naapurijono

if __name__ == "__main__":
    lista = [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25]
    print(pisin_naapurijono(lista))
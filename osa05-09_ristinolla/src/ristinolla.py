# tee ratkaisu tänne
def pelaa_siirto(lauta: list, x: int, y: int, nappula: str) -> bool:
    x_sisalla = False
    y_sisalla = False
    nappula_laitettu = False

    if(0 <= x and x <= 2):
        x_sisalla = True
    if(0 <= y and y <= 2):
        y_sisalla = True
    
    if(x_sisalla and y_sisalla):
        if(lauta[y][x] == ""):
            lauta[y][x] = nappula
            nappula_laitettu = True

    return nappula_laitettu
    
if __name__ == "__main__":
    lauta = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(pelaa_siirto(lauta, 2, 0, "X"))
    print(lauta)
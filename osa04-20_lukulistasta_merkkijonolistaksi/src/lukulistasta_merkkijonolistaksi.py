# tee ratkaisu tänne
def muotoile(lista):
    muotoiltu_lista = []
    for luku in lista:
        muotoiltu_lista.append(f"{luku:.2f}")
    return muotoiltu_lista

if __name__ == "__main__":
    print(muotoile([1.234, 0.3333, 0.11111, 3.446]))
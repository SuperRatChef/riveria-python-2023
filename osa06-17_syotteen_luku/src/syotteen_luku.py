# tee ratkaisu tänne
def lue(kysymys: str, alku: int, loppu: int) -> int:
    while True:
        try:
            syote = input("syötä luku: ")
            luku = int(syote)
            if(alku < luku and luku < loppu):
                return luku
        except ValueError:
            pass # tämä komento ei tee mitään

        print(f"Syötteen on oltava kokonaisluku väliltä {alku}...{loppu}")


if __name__ == "__main__":
    luku = lue("syltö luku: ", 5, 10)
    print("syötit luvun:",luku)


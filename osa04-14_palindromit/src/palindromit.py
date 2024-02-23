# tee ratkaisu tänne
# huomaa, että tällä kertaa pääohjelmaa ei tule kirjoittaa lohkon
# if __name__ == "__main__":
# sisälle!
def palindromi(sana: str):
    yritys = list(sana)
    yritys_reversed = yritys[::-1]
    if(yritys == yritys_reversed):
        return True
    else:
        return False

while(True):
    sana = input("Anna palindromi: ")
    #print(yritys)
    #print(yritys_reversed)
    onkoPalindromi = palindromi(sana)
    
    if(onkoPalindromi):
        print(f"{sana} on palindromi!")
        break
    else:
        print("ei ollut palindromi")
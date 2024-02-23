# Tee ratkaisu tänne
def anagrammi(sana1, sana2):
    list1 = sorted(list(sana1))
    list2 = sorted(list(sana2))
    if(list1 == list2):
        return True
    else:
        return False
if __name__ == "__main__":
    print(anagrammi("talo", "tolaa"))
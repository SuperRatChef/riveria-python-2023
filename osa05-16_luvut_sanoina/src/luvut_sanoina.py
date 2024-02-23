# tee ratkaisu tänne

def lukukirja():
    ykköset = {
        0: "nolla",
        1: "yksi",
        2: "kaksi",
        3: "kolme",
        4: "neljä",
        5: "viisi",
        6: "kuusi",
        7: "seitsemän",
        8: "kahdeksan",
        9: "yhdeksän",
        10: "kymmenen"
    }

    lukukirja = {}

    for i in range(100):
        if(0 <= i and i <= 10):
            lukukirja[i] = ykköset[i]
        elif(11 <= i and i <= 19):
            lukukirja[i] = ykköset[i-10]+"toista"
        elif(20 <= i and i <= 99):
            if(i % 10 == 0):
                lukukirja[i] = ykköset[i/10]+"kymmentä"
            else:
                lukukirja[i] = ykköset[i//10]+"kymmentä"+ykköset[i-(i//10*10)]

    return lukukirja


if __name__ == "__main__":
    luvut = lukukirja()
    print(luvut[2])
    print(luvut[11])
    print(luvut[45])
    print(luvut[99])
    print(luvut[0])
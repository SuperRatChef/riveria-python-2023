# tee ratkaisu tänne

def etsi_elokuvat(rekisteri: list, hakusana: str):
    tulokset = []
    for objekti in rekisteri:
        if(hakusana.lower() in objekti["nimi"].lower()):
            tulokset.append(objekti)
    return tulokset

if __name__ == "__main__":
    rekisteri = [{"nimi": "Pythonin viemää", "ohjaaja": "Pekka Python", "vuosi": 2017, "pituus": 116},
    {"nimi": "Python lentokoneessa", "ohjaaja": "Renny Pythonen", "vuosi": 2001, "pituus": 94},
    {"nimi": "Koodaajien yö", "ohjaaja": "M. Night Python", "vuosi": 2011, "pituus": 101}]

    lista = etsi_elokuvat(rekisteri, "python")
    print(lista)
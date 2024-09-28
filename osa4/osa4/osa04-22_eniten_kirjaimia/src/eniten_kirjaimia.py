# tee ratkaisu tänne

def eniten_kirjainta(mjono: str):
    eniten = ""
    eniten_maara = 0
    for kirjain in mjono:
        maara = mjono.count(kirjain)
        if maara > eniten_maara:
            eniten = kirjain
            eniten_maara = maara
    return eniten

if __name__ == "__main__":
    toinen_jono = "esimerkkimerkkijonokki"
    print(eniten_kirjainta(toinen_jono))
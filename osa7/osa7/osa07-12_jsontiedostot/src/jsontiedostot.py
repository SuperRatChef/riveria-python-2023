# tee ratkaisu tänne
import json

def tulosta_henkilot(tiedosto: str):
    with open(tiedosto) as file:
        data = file.read()
    opiskelijat = json.loads(data)

    for opiskelija in opiskelijat:
        nimi = opiskelija["nimi"]
        ika = opiskelija["ika"]
        harrastukset = opiskelija["harrastukset"]

        print(f"{nimi} {ika} vuotta ({", ".join(harrastukset)})")

if __name__ == "__main__":
    tulosta_henkilot("tiedosto1.json")
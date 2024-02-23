# tee ratkaisu tänne
def histogrammi(merkkijono: str):
    histogrammi = {}
    for kirjain in merkkijono:
        if kirjain not in histogrammi:
            histogrammi[kirjain] = 1
        else:
            histogrammi[kirjain] += 1
    
    for kirjain, arvo in histogrammi.items():
        print(f"{kirjain} {"*"*arvo}")

if __name__ == "__main__":
    histogrammi("saippuakauppias")
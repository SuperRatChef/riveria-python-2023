# Kirjoita ratkaisu tähän

lahjan_suuruus = int(input("Lahjan suuruus? "))

veron_alaraja = 0
vero_alarajalla = 0
ylimenevä_osuus = 0
ylimenevä_prosentti = 0
veroa_yhteensä = 0
onko_veroa = False

if(lahjan_suuruus < 5000):
    onko_veroa = False
elif(5000 <= lahjan_suuruus and lahjan_suuruus <= 25000):
    veron_alaraja = 5000
    vero_alarajalla = 100
    ylimenevä_prosentti = 8
    onko_veroa = True
elif(25000 <= lahjan_suuruus and lahjan_suuruus <= 55000):
    veron_alaraja = 25000
    vero_alarajalla = 1700
    ylimenevä_prosentti = 10
    onko_veroa = True
elif(55000 <= lahjan_suuruus and lahjan_suuruus <= 200000):
    veron_alaraja = 55000
    vero_alarajalla = 4700
    ylimenevä_prosentti = 12
    onko_veroa = True
elif(200000 <= lahjan_suuruus and lahjan_suuruus <= 1000000):
    veron_alaraja = 200000
    vero_alarajalla = 22100
    ylimenevä_prosentti = 15
    onko_veroa = True
else:
    veron_alaraja = 1000000
    vero_alarajalla = 142100
    ylimenevä_prosentti = 17
    onko_veroa = True

if(onko_veroa):
    ylimenevä_osuus = lahjan_suuruus - veron_alaraja
    veroa_yhteensä = vero_alarajalla + (ylimenevä_osuus * ylimenevä_prosentti/100)
    print("Vero:",veroa_yhteensä,"euroa")
else:
    print("Ei veroa!")


# Kirjoita ratkaisu tähän
montako_kertaa = int(input("Montako kertaa viikossa syöt Unicafessa?"))
hinta = float(input("Unicafe-lounaan hinta"))
ruokaostokset = float(input("Paljonko käytät viikossa ruokaostoksiin?"))
viikkokustannus = montako_kertaa * hinta + ruokaostokset
päiväkustannus = viikkokustannus/7
 
print("")
print("Kustannukset keskimäärin:")
print(f"Päivässä {päiväkustannus} euroa")
print(f"Viikossa {viikkokustannus} euroa")

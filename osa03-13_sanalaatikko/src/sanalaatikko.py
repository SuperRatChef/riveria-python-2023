# Kirjoita ratkaisu tähän


sana = input("sana")
pad_oikea = " "*int((28-len(sana))/2)
pad_vasen = " "*(28-len(sana)-len(pad_oikea))

print("*"*30)
print(f"*{pad_oikea}{sana}{pad_vasen}*")
print("*"*30)

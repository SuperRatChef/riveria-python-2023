# Kirjoita ratkaisu tähän
fahrenheit = int(input("anna lämpötila (F): "))
celcius = (fahrenheit - 32) * 5/9

print(f"{fahrenheit} fahrenheit-astetta on {celcius} celsius-astetta")
if(celcius < 0):
    print("Paleltaa!")
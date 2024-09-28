# Kirjoita ratkaisu tähän

lause = input("Anna lause: ")
kirjain = ""
iteraattori = 0

while(iteraattori < len(lause)):
    kirjain = lause[iteraattori]
    if(kirjain == " "):
        print(lause[iteraattori+1])
    if(iteraattori == 0):
        print(lause[iteraattori])
    iteraattori += 1
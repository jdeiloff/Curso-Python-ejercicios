cadena = 'Geringoso'
capadepenapa = ''

for c in cadena:
    capadepenapa = capadepenapa + c
    if "e" in c:
       capadepenapa = capadepenapa + "pe"
    elif "a" in c:
       capadepenapa = capadepenapa + "pa"
    elif "i" in c:
        capadepenapa = capadepenapa + "pi"
    elif "o" in c:
        capadepenapa = capadepenapa + "po"
    elif "u" in c:
        capadepenapa = capadepenapa + "pu"

print(capadepenapa)





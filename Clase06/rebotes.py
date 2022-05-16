altura_rebote = 100 # Altura desde la que se tira la pelota
rebote = 1 # Numero de rebote
altura_n = 100

while rebote <= 10:
    print(rebote, round(altura_n * (3/5), 4))
    rebote = rebote + 1
    altura_n = altura_n * (3/5)
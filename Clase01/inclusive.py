frase = 'todos somos programadores'
palabras = frase.split()
frase_t = ""
for palabra in palabras:
    if  "o" in palabra[-2:]:
        palabra = "e".join(palabra.rsplit("o", 1))
        print(palabra)

frase_t = "".join(palabra)

print(frase_t)
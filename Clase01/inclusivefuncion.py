# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 21:57:15 2021

@author: Jony
"""
def neutralizar_palabra(palabra):
    if len(palabra)>=2:
        if palabra[-2]=='o':
            palabra_nueva = palabra[:-2]+'e'+palabra[-1]
        elif palabra [-1]=='o':
            palabra_nueva = palabra[:-1]+'e'
        else:
            palabra_nueva = palabra
        return palabra_nueva

frase = 'blalblabal elel lololo lalalala'
palabras = frase.split()
palabras_nuevas = []
for palabra in palabras:
    palabra_nueva = neutralizar_palabra(palabra)
    palabras_nuevas.append(palabra_nueva)
frase_t = ' '.join(palabras_nuevas)
print(frase_t)
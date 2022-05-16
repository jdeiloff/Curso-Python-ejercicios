# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 19:28:50 2021

@author: Jony
"""

# De una lista, devuelve un diccionario con la palabra original como key y la traduccion en geringoso como value.
lista = ['banana', 'manzana', 'mandarina']
cadena= ",".join(lista) # Separa la lista en string para poder ser procesada por el traductor geringoso.
capadepenapa = ''


for c in cadena:
    capadepenapa += c # el += reemplaza a capa.. = capa... + c
    if c in "aeiou":
        capadepenapa += "p" + c # Mucho mas simplificado, si hay una vocal, agrego "p" mas la vocal a la cadena.
    elif c in "AEIOU":
        capadepenapa += "P" + c # Tengo en cuenta los casos con mayusculas.

dicgeringoso = dict(zip(cadena.split(","), capadepenapa.split(","))) # Uno cadena y capadepenapa con .split() para volverlos una lista. La funcion zip() asocia un par de valores, uno de cada lista, a una tupla, con dict() lo vuelvo diccionario. 
print(dicgeringoso)
        



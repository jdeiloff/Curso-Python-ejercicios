# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 14:33:08 2021

@author: Jony
"""


import csv
from collections import Counter

def leer_parque(lista_arboles, parque):
        lista = []
        with open(lista_arboles, 'rt', encoding="utf8") as f:
            filasarboles = csv.reader(f)
            headers = next(f)
            for datos in filasarboles:
                registro = dict(zip(headers, filasarboles))
                if parque.lower() in (datos[10]).lower():
                    lista.append(registro)
        return lista
#%%
gral_paz = ('../Data/arbolado-en-espacios-verdes.csv')
len(gral_paz)

#%% 
def especies(lista_arboles):
    lista = []
    for arbol in lista_arboles:
        lista.append(arbol['nombre_com'])
    return set(lista)

#%% 
def contar_ejemplares(lista_arboles):
    d = Counter()
    for arbol in lista_arboles:
        d[arbol['nombre_com']] += 1
    return d

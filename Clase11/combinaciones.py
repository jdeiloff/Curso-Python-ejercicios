# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 14:26:46 2021

@author: Jony
"""

#%%11.10

def combinaciones(lista, k):
    if len(lista) == 1:
        comb = [lista[0]*k]
    elif k == 1:
        comb == lista
    else:
        comb = combinaciones([lista[0], combinaciones(lista[1:], k-1)], 2)
    return comb

print(combinaciones)

#%% otro (combinaciones de largo k con todos los elementos de la lista)
def combinaciones(lista,k):
    if k == 1:
        comb = lista
    else:
        comb_rec = combinaciones(lista, k-1)
        comb = [e + c for e in lista for c in comb_rec]
    return comb
#%% Combinaciones de largo 3 con la lista a,b,c
print(combinaciones(['a, b', 'c'], 3))

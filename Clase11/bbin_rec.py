# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 22:22:52 2021

@author: Jony
"""

def bbinaria_rec(lista, e):
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
    # completar
        if lista[medio] <= e:
            lista = lista[medio:]
        else:
            lista= lista[:medio]
        bbinaria_rec(lista,e)
        res = bbinaria_rec(lista,e)
    return res

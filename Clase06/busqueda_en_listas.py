# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 01:51:10 2021

@author: Jony
"""

def busqueda_lineal_lordenada(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z >= e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos

def eliminar_derecha(lista, e):
    listac = lista.copy()
    pos = (busqueda_lineal_lordenada(listac,e))
    listac[pos+1: -1]=[]
    return listac

eliminar_derecha([1, 3, 5, 7], 0)
lista = [1, 3, 5, 7]
e = 0

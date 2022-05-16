# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 18:46:20 2021

@author: Jony
"""
# Funcion propagar que recibe un vector con 0s, 1s y -1s y devuelva un vector en el que los 1s se propagaron a sus vecinos con 0.
# Le tengo que cambiar unas cosas quedo muy berreta, no propaga 1s si están más allá de 2 posiciones.
def propagar(lista):
    original = lista
    for pos, elem in enumerate(original):
        if (elem == 1) and not (original[pos-1]==-1) and not(original[pos-2]==-1): # Approach bastante berreta, cambiar por otro.
           original[pos-1] = 1
           original[pos-2] = 1
        elif (elem == 1) and not (original[pos+1]==-1) and not(original[pos+2]==-1):
           original[pos+1] = 1
           original[pos+2] = 1
        elif (elem == 0) and not (-1 in original): # Parche trucho que propaga todos los 1s si hay alguno y no hay -1s.
            original[pos] = 1
    return original

                    
# propagar([ 0, 1, 1,-1, 0, 0, 0, 0,-1, 1, 0, 0, 0])
# propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
# propagar([ 0, 0, 0, 1, 0, 0])

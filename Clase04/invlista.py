# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 16:22:22 2021

@author: Jony
"""

# Ej 4.5 Invertir lista

def invertir_lista(lista): # Invierte orden de una lista (basado en material de Unidad 4.2, del curso Programacion en Python, UNSaM). Si le das por ejemplo ['Bogotá', 'Santiago', 'San Fernando', 'San Miguel'], devuelve ['San Miguel', 'San Fernando', 'Santiago', 'Bogotá'].
    invertida = [] # Declaro la lista invertida
    original = lista # Copia la lista original para evitar modificarla
    i = len(lista)
    while i > 0:    # Empiezo desde el último elemento.
        i = i-1
        invertida.append (original.pop(i))  # aca modifica la copia de la lista original eliminando el ultimo elemento
    return invertida

# invertir_lista([1, 2, 3, 4, 5])
# invertir_lista(['Bogotá', 'Santiago', 'San Fernando', 'San Miguel'])

#%% Otra versión

def invertir_listav2(lista):
    invertida = []
    for e in lista:
        invertida = [e] + invertida
    return invertida
#%% Otra versión más

def invertir_listav3(lista):
    invertida = []
    for i in range(len(lista)-1, -1, -1):
        invertida.append(lista[i])
    return invertida

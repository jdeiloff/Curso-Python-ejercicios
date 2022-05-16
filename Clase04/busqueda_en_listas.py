# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 13:45:28 2021

@author: Jony
"""

def buscar_u_elemento(lista, u): # Busca un elemento u en una lista y devuelve su posición si está, sino devuelve -1 (ejemplo de ([1, 1, 2, -4, -5], 2) devuelve 2).
    pos = -1 # Valor por defecto -1 por si no está u.
    for ind, elem in enumerate(lista): # Itero la lista y voy enumerando las posiciones.
       if u == elem:
           pos = ind
           break # Si lo encuentro, termino el proceso.
    return pos # Devuelvo la posición, o -1 si no está.

def buscar_n_elemento(lista, n): # Busca un elemento n en una lista y devuelve cuantas veces aparece en la lista (ejemplo de ([1, 1, 2, -4, -5], 1) devuelve 2).
    contador = 0 # Inicia Contador
    for elemen in lista: # Itero la lista
        if elemen == n: # Si esta n...
            contador += 1 # contador aumenta en 1.
    return contador # Devuelve cuantas veces aparece n.

def maximo(lista): # Devuelve el máximo de una lista, la lista debe ser no vacía(ejemplo de [1, 1, 2, -4, -5] devuelve 2).
    m = lista[0] # Inicializa valor maximo en el primer valor de la lista.
    for e in lista: # Itera la lista
        if e > m: # Si el valor iterado es mayor al maximo valor m...
            m = e # ese valor es el nuevo maximo m.
    return m # Devuelve m.

def minimo(lista): # Devuelve valor mínimo de una lista no vacía (ejemplo de [1, 1, 2, -4, -5] devuelve -5).
    chiqui = lista[0] # Inicia el valor mas chiquito (no uso min por estar reservado) en el primer valor de la lista
    for l in lista:
        if l < chiqui:
            chiqui = l
    return chiqui

# minimo([-4, -5])        
buscar_n_elemento([1,2,3,2,3,3],9)

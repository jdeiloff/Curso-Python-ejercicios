# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 22:42:30 2021

@author: Jony
"""

'''
Ordena una lista dada por el método de burbujeo (va comparando de a pares, si el primer elemento es
mayor al siguiente, lo coloca a su derecha hasta terminar la lista).
En el peor de los casos, toda la lista está invertida y tiene que ordenar todos los pares de valores
lo que sería un orden de N. En el mejor de los casos, la lista ya está ordenada y no hay que ordenar
ningún par de valores. No voy a hacer el extra, me empaqué con la recursión, para la próxima.
'''

def ord_burbujeo(lista):
    n = len(lista)
    for i in range(n-1): # Itero sobre la lista (si i esta al final de la lista queda ahi)
        for j in range(0, n-i-1): # Itera la lista desde el primer elemento hasta n-i-1
            if lista[j] > lista[j + 1] : # Si el primer elemento es mayor al siguiente, lo intercambia
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
 
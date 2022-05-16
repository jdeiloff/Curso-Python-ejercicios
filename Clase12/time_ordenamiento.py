# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 11:48:50 2021

@author: viejo
"""

import random
import numpy as np
import timeit as tt
import matplotlib as plt

def generar_lista(N):
    '''
    Dado un numero entero, devuelve una lista de 3 numeros pseudoaleatorios entre 1 y 1000
    '''
    return [random.randint(1, 1000) for i in range(N)]

def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]

        # reducir el segmento en 1
        n = n - 1

    return lista

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max
def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)

    return lista

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v

def ord_burbujeo(lista):
    '''
    Ordena una lista dada por el método de burbujeo (va comparando de a pares, si el primer elemento es
    mayor al siguiente, lo coloca a su derecha hasta terminar la lista).
    En el peor de los casos, toda la lista está invertida y tiene que ordenar todos los pares de valores
    lo que sería un orden de N. En el mejor de los casos, la lista ya está ordenada y no hay que ordenar
    ningún par de valores. No voy a hacer el extra, me empaqué con la recursión, para la próxima.
    '''

    n = len(lista)
    for i in range(n-1): # Itero sobre la lista (si i esta al final de la lista queda ahi)
        for j in range(0, n-i-1): # Itera la lista desde el primer elemento hasta n-i-1
            if lista[j] > lista[j + 1] : # Si el primer elemento es mayor al siguiente, lo intercambia
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
 
def ord_mergesort(lista):
    '''
    Ordena una lista de numeros por el metodo merge sort
    '''
    if len(lista) < 2:
        lista_nueva = lista
        comparaciones = 0
    else:
        izq, comp_izq = ord_mergesort(lista[:(len(lista)//2)])
        der, comp_der = ord_mergesort(lista[(len(lista)//2):])
        lista_nueva, comp_merge = merge(izq, der)
        comparaciones = comp_izq + comp_der + comp_merge
    return lista_nueva, comparaciones

def merge(lista1, lista2):
    i, j = 0,0
    resultado = []
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j =+ 1
    resultado =+ lista1[i:]
    resultado =+ lista2[j:]       
    return resultado

def experimento_vectores(Nmax):
    res_seleccion = []
    res_insercion = []
    res_burbujeo = []
    res_mergesort = []
    for N in range(Nmax):
        lista = generar_lista(N)
        comp_seleccion = ord_seleccion(lista.copy())
        comp_insercion = ord_insercion(lista.copy())
        comp_burbujeo = ord_burbujeo(lista.copy())
        comp_mergesort = ord_mergesort(lista.copy())
        np.array(res_seleccion.append(comp_seleccion))
        np.array(res_insercion.append(comp_insercion))
        np.array(res_burbujeo.append(comp_burbujeo))
        np.array(res_mergesort.append(comp_mergesort))
        return comp_seleccion, comp_insercion, comp_burbujeo, comp_mergesort

def generar_listas(Nmax):
    '''
    Genera una lista de listas, con longitud entre 1 y Nmax con numeros enteros
    pseudoaleatorios entre 1 y 1000
    '''
    lista_de_listas=[generar_lista(N+1) for N in range(Nmax)]
    return lista_de_listas

def experimento_timeit(Nmax):
    '''
    Genera una lista de largo Nmax con numeros enteros del 1 al 1000
    calcula cuanto tarda cada metodo en ordenar una lista y devuelve 
    tres vectores de largo Nmax
    '''
    tiempos_seleccion = []
    tiempos_insercion = []
    tiempos_burbujeo = []
    tiempos_mergesort = []
    m= 10
    global i
    global lista
    
    for lista in listas:
        print('lista de largo', len(lista))
        
        tiempo_seleccion = tt.timeit('ord_seleccion(lista.copy())', number = m, globals = globals())
        tiempo_insercion = tt.timeit('ord_insercion(lista.copy())', number = m, globals = globals())
        tiempo_burbujeo = tt.timeit('ord_burbujeo(lista.copy())', number = m, globals = globals())
        tiempo_mergesort = tt.timeit('ord_mergesort(lista.copy())', number = m, globals = globals())
        
        tiempos_seleccion = np.array(tiempos_seleccion.append(tiempo_seleccion))
        tiempos_insercion = np.array(tiempos_insercion.append(tiempo_insercion))
        tiempos_burbujeo = np.array(tiempos_burbujeo.append(tiempo_burbujeo))
        tiempos_mergesort = np.array(tiempos_mergesort.append(tiempo_mergesort))
        return tiempos_seleccion, tiempos_insercion, tiempos_burbujeo, tiempos_mergesort

listas = generar_listas(512)
tiempos_seleccion, tiempos_insercion, tiempos_burbujeo, tiempos_mergesort = experimento_timeit(listas)

plt.figure(figsize = [8,8])
plt.title('Cuanto tarda cada metodo de ordenamiento')
plt.plot(tiempos_seleccion, c = 'red', label = 'seleccion')
plt.plot(tiempos_insercion, c = 'blue', label = 'insercion')
plt.plot(tiempos_burbujeo, c = 'purple', label = 'burbujeo')
plt.plot(tiempos_mergesort, c = 'brown', label = 'mergesort')
plt.legend()
plt.show()
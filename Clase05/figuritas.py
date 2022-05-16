# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 16:38:07 2021

@author: Jony
"""

import random
import numpy as np
import matplotlib as plt

figus_sobre = 1
n_repeticiones = 1000

def crear_album(figus_total): # Crea un album vacio de figuritas con figus_total numero de figus.
    return np.zeros(figus_total, dtype=int)

def album_incompleto(A): # Chequea si el album esta completo (devuelve False) o si le falta alguna figu (devuelve True)
    return (A < 1).any()

def comprar_figu(figus_total): # Genera del total de figus, un sobre con figuritas
    return random.randint(1, range(figus_total))

def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    sobres = 0
    while album_incompleto(album) == True:
        album[comprar_figu(figus_total)] +=1
        sobres += 1
    return sobres

def repetir(n_repeticiones):
    n_sobres = []
    for i in range(n_repeticiones):
        n_sobres.append(cuantas_figus(6))
    return np.mean(n_sobres)

#o=repetir(1000)

def experimento_figus(n_repeticiones, figus_total):
    n_sobres = []
    for i in range(n_repeticiones):
        n_sobres.append(cuantas_figus(figus_total))
    return np.mean(n_sobres)

def comprar_paquete(figus_total, figus_paquete):
    p = []
    for i in range(figus_paquete):
        p.append(comprar_figu(figus_total))
    return p

def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] += 1
    return album.sum()/figus_paquete

'''
figus_total = 670
n_repeticiones = 100

l = []

for i in range(n_repeticiones):
    l.append(cuantas_figus(figus_total))
    
    print(f'Para llenar un álbum de {figus_total} figus compré en promedio {np.mean(l)} figus')
'''

def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] += 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)
    return historia_figus_pegadas

# plt.plot(calcular_historia_figus_pegadas(figus_total,figus_paquete))








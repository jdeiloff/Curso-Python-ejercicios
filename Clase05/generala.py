# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 13:02:41 2021

@author: viejo
"""

#%% Ejercicio 5.2 Generala: Simula tirar 3 veces los 5 dados y ver cuántas veces se obtuvieron 5 dados iguales
# La probabilidad sería para cada dado p=(1/5)^5
import random

def tirar():
    tirada = []
    for i in range(5):
        tirada.append(random.randint(1,6))
    return tirada

def juntar_iguales(tirada):
    lista = []
    for i in range(1,7):
        lista.append(tirada.count(i))
    for j, e in enumerate(lista):
        if e == max(lista):
            res = [j+1]*e
    return res

def mejorar_tirada(tirada):
    repe = juntar_iguales(tirada)
    l = tirar(5-len(repe))
    t = repe + l
    return t

def generala():
    t = tirar(5)
    t = mejorar_tirada(t)
    t = mejorar_tirada(t)
    return es_generala(t)

def es_generala(tirada):
    return max(tirada) == min(tirada)


def prob_generala(N):
    N = int(N)
    G = sum([es_generala(tirar()) for i in range(N)])
    prob = G/N
    return prob

p= prob_generala(100000)
#%%
'''
N = 100000
salio_generala_servida = [es_generala(tirar()) for i in range(N)]
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
'''
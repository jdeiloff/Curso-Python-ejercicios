# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 12:04:02 2021

@author: Jony
"""
                                                                                           
import random

dado = random.randint(1,6) # Da un valor entero pseudoaleatorio entre 1 y 6.

# GENERALA simula tirar 5 dados y devuelve valores al azar.

tirada =[]
for i in range(5):
    tirada.append(random.randint(1,6))
print(tirada)

#%% Generala servida: Simula tirar varias veces los dados y ver cuántas veces se obtuvieron 5 dados iguales
# La probabilidad sería para cada dado p=(1/5)^5

def tirar():
    tirada = []
    for i in range(5):
        tirada.append(random.randint(1,6))
    return tirada

def es_generala(tirada):
    return max(tirada) == min(tirada)


N = 100000
salio_generala_servida = [es_generala(tirar()) for i in range(N)]
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 20:23:49 2021

@author: Jony
"""
import random

def generar_punto(): # Genera puntos aleatorios sobre dos ejes.
    x = random.random()
    y = random.random()
    return x,y

def generar(N): # Genera N veces los puntos aleatorios con generar_punto().
    puntos=[]
    for i in range(N):
        puntos.append(generar_punto())
    return puntos

def circulo(): # Devuelve una lista donde están todos los puntos que caen en el círculo de radio 1.
    a=[]
    b=[]
    for x, y in generar(100000):
        if ((x**2 + y**2)<1):
            a.append(x)
            b.append(y)
        circulo = a + b
    return circulo

m = len(circulo()) # Cuantos puntos estan en el circulo.
N = 100000 # Cuantos puntos se generaron
pi = ((4*m)/N)/2 # Valor de pi aproximado.
print(f'Con un circulo de {N} puntos, pi vale: {pi}')


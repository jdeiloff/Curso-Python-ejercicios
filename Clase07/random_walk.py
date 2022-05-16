# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 01:08:44 2021

@author: Jony
"""

import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

N = 100000


# GRAFICOS TERMINAR
fig = plt.figure()
plt.subplot(2, 1, 1) # define la figura de arriba
plt.plot(randomwalk(N)) # dibuja la curva
plt.xticks([]), plt.yticks([]) # saca las marcas

plt.subplot(2, 2, 3) # define la primera de abajo, que sería la tercera si fuera una grilla regular de 2x2
plt.plot([0,1],[0,1])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 4) # define la segunda de abajo, que sería la cuarta figura si fuera una grilla regular de 2x2
plt.plot([0,1],[1,0])
plt.xticks([]), plt.yticks([])

plt.show()

#%% DEFINICION CAMINOS
def camino_lejos(lista):
    c_max = [(max(map(abs, caminata)),caminata) for caminata in lista]
    return max(c_max)[1]
def camino_cerca(lista):
    c_max = [(max(map(abs, caminata)),caminata) for caminata in lista]
    return min(c_max)[1]
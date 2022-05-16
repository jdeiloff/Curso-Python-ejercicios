# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 18:05:08 2021

@author: Jony
"""
import random
import numpy as np
  
def medir_temp(n):  # Guarda un array con los valores de temperatura con distribución normal con media 37.5 y desvío de 0.2 en un archivo temperaturas.npy.
    val_temp=[]
    for i in range(n):
        val_temp.append(random.normalvariate(37.5,0.2))
    np.save('temperaturas', np.array(val_temp))
    return val_temp

def resumen_temp(n): # Va generando con numpy una tupla con valor maximo, minimo, media y promedio de temperatura generados con medir_temp(n).
    valores = np.array(medir_temp(n))
    tupla = ((np.max(valores)), (np.min(valores)), np.mean(valores), np.average(valores))
    return tupla

# lolo = resumen_temp(35)
# Ej_58 = medir_temp(999)

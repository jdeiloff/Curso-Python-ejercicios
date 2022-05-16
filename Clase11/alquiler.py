# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 00:33:36 2021

@author: Jony
"""

import numpy as np
import matplotlib.pyplot as plt

def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b

superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])

c, d = ajuste_lineal_simple(superficie, alquiler)
grilla_x = np.linspace(start = 65, stop = 180, num = 1000)
grilla_y = grilla_x*c + d
errores = alquiler - (c*superficie + d)

graf = plt.scatter(x = superficie, y = alquiler)
plt.title('Precio de alquiler por superficie')
plt.plot(grilla_x, grilla_y, c = 'purple')
plt.xlabel('Alquiler')
plt.ylabel('Superficie')
plt.show()
print(errores)
print("ECM:", (errores**2).mean())




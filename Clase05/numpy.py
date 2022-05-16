# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 12:23:38 2021

@author: Jony
"""

import numpy as np


a = np.array([1, 2, 3]) # transforma la lista dada en array, np trabaja con arrays (vectores/matrices) con elementos float64 si no le especificas formato
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) # Da una matriz de 3 filas x 4 columnas
np.empty(2) # Crea un arreglo con dos elementos
# imprime array([ 3.14, 42.  ])   puede variar

x = np.ones(2, dtype=np.int64) # Crea vector con ceros, dtype=np.(tipo de elemento) int de 64 bits en este caso

np.arange(2, 9, 2) # o np.arange(2, 10, 2), crea vector con (primer numero, limite donde no llega, paso)
# imprime array([2, 4, 6, 8])

np.linspace(0, 10, num=5) # Crea un vector con (primer numero, ultimo numero, cantidad de elementos). (similar al anterior pero distinto formato)

# imprime array([ 0. ,  2.5,  5. ,  7.5, 10. ])

#♠ Ejercicio 5.7. Generá un vector que tenga los números impares entre el 1 y el 19 inclusive usando arange(). Repetí el ejercicio usando linspace()
np.arange(1, 20, 2)
#• imprime array([ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19])

np.linspace(1, 19, num=10)
#○ imprime array([ 1.,  3.,  5.,  7.,  9., 11., 13., 15., 17., 19.])

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
np.sort(arr) # Ordena array (no modificó arr, solo devolvio una copia ordenada)
# imprime array([1, 2, 3, 4, 5, 6, 7, 8])

a = np.array([1, 2, 3, 4]) # Genera array a
b = np.array([5, 6, 7, 8]) # Genera array b
np.concatenate((a, b)) # Concatena array a con b
# imprime array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
np.concatenate((x, y), axis=0) # Concatena ambos pares de datos
# imprime array([[1, 2],
#                [3, 4],
#                [5, 6]])

# ndarray.ndim da dimension de array
# ndarray.shape da cantidad de elementos de cada eje (ej (2,3) significa 2 filas 3 columnas)
# ndarray.size da el resultado de multiplicar filas * columnas

#%%Cambia Forma
a = np.arange(6) 
# imprime [0 1 2 3 4 5]

b = a.reshape(3, 2) # Reordena el array como 3 filas, 2 columnas pero con el mismo numero de elementos (debe ser compatible con este ultimo dato)
# Imprime
#[[0 1]
# [2 3]
# [4 5]]

a = np.array([1, 2, 3, 4, 5, 6])
vec_fila = a[np.newaxis, :] # newaxis agrega una dimension convirtiendolo en fila
vec_fila.shape
# imprime (1, 6)
vec_col = a[:, np.newaxis]  # Asi lo convierte en columna

#%%
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) # genera array
print(a[a < 5]) # Da los menores a 5
# imprime [1 2 3 4]
pares = a[a%2==0] # imprime solo los pares
five_up = (a > 5) | (a == 5) # Pido mayores a 5 o que sea igual a 5 (| es o, & es y)

b = np.nonzero(a < 5) # nonzero imrpime los indices (coordenadas, posiciones), en este caso de los menores a 5, si ninguna satisface, devuelve un array vacío.
# imprime (array([0, 0, 0, 0]), array([0, 1, 2, 3]))

lista_de_coordenadas = list(zip(b[0], b[1])) # Pasa las coordenadas donde estan esos elementos y los pasa a una lista

arr1 = a[3:8] # pido una parte del array entre 3(no incluido) y 8(si incluido), pero se lo arranco al array original, por lo que si modifico arr1, modifico mi array original a, OJO haceer copia primero!! (usar ej b2 = a[1, :].copy())
# Imprime array([4, 5, 6, 7, 8])

#%% Operaciones
b.sum(axis=0) # suma elementos de cada columna
b.sum(axis=1) # suma elementos de cada fila

# Multiplicacion escalar si no son compatibles los datos da ValueError
data = np.arrray([1.0, 2.0])
data * 1.6
# imprime array([1.6, 3.2])

np.random.random(3) # Genera array con 3 valores aleatorios.

# Error cuadrático medio
error = (1/n) * np.sum(np.square(predictions - labels)) # Donde n es el numero de elementos, predictions el valor del modelo y labels valores de las mediciones reales.

# Guardar arrays como archivos (save/load genera/carga .npy binarios pequeños y savetxt/loadtxt archivos de texto)
a = np.array([1, 2, 3, 4, 5, 6])
np.save('filename', a) # Lo guarda
b = np.load('filename.npy') # Lo carga
np.savetxt('new_file.csv', csv_arr) # Lo guarda como archivo txt en formato.csv
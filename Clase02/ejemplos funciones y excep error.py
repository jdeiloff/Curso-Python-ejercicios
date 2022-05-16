# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 20:07:04 2021

@author: Jony
"""

def preguntar_edad(nombre):
    edad = int(input(f'ingresá tu edad {nombre}: '))
    if edad<0:
        raise ValueError('La edad no puede ser negativa.')
    return edad

#%%

for nombre in ['Pedro','Juan','Caballero']:
    try:
        edad = preguntar_edad(nombre)
        print(f'{nombre} tiene {edad} años.')
    except ValueError:
        print(f'{nombre} no ingresó una edad válida.')

#%%

# Python3 program to Convert a
# list to dictionary
 
def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct
         
# Driver code
lst = ['a', 1, 'b', 2, 'c', 3]
print(Convert(lst))

#%%

# Python3 program to Convert a
# list to dictionary
 
def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct
         
# Driver code
lst = ['a', 1, 'b', 2, 'c', 3]
print(Convert(lst))
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 20:28:03 2021

@author: Jony
"""
numero_valido=False
while not numero_valido:
    try:
        a = input('Ingresá un número entero: ')
        n = int(a)
        numero_valido = True
    except ValueError:
        print('No es válido. Intentá de nuevo.')
print(f'Ingresaste {n}.')

raise RuntimeError('¡Qué moco!')
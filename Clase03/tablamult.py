# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 11:41:09 2021

@author: Jony
"""
#intento de suma
#for i in range(10):
#    print(f'{i:>3d}', end= ' ')
#    print(i+i)
#print('-'*40)

#%%


print(' '*5, end='')
m = 0
for i in range(10):                # Genera los encabezados y luego los imprime.
    print (f'{i:>4d}', end='')
print()
print('-'*(46))                            # Genera linea separadora de los encabezados.
for l in range(10):               # Multiplicacion (CAMBIAR POR SUMA)
    print(f'{l:>4d}:', end='')
    for n in range(10):
        m = l * n
        print(f'{m:>4d}', end='')
    print ('')
    
    
#%%

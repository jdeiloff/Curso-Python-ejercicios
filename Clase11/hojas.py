# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 15:35:14 2021

@author: Jony
"""

def medidas_hoja_A(n):
    if n == 0:
        return 841, 1189
    ancho_ant, largo_ant = medidas_hoja_A(n-1)
    ancho = largo_ant //2
    largo = ancho_ant
    return ancho, largo

#%%
print(medidas_hojas_A(4))
#%% ejercicio 11.13 otra vers

def medidas_hojas_A(n):
    if n == 0:
        return 841, 1189
    ancho_ant, largo_ant = medidas_hoja_A(n-1)
    #anchi = largo_ant //2
    # largo = ancho_ant
    return largo_ant//2,ancho_ant
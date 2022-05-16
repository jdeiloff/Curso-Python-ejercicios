# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 15:35:14 2021

@author: Jony
"""

def medidas_hoja_A(N):
    '''
    Recibe un entero N mayor a cero, devuelve ancho y largo de una hoja ISO An.
    '''
    if N == 0:
        return 841, 1189
    ancho_ant, largo_ant = medidas_hoja_A(N-1)
    ancho = largo_ant //2
    largo = ancho_ant
    return ancho, largo


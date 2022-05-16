#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 23:00:26 2021

@author: Jony
"""

import informe_final
import sys

def costo_camion(filename):
    '''
    Computa el precio total (cantidad * precio) de un archivo camion
    '''
    camion = informe_final.leer_camion(filename)
    return camion.precio_total()

def f_principal(parametros):
    if len(parametros) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion')
        print('uso inadecuado, revisar argumentos.')
    else:
        camion = parametros[1]
        costo_camion(camion)
    return costo_camion(camion)
    
if __name__ == '__main__':
    f_principal(sys.argv)
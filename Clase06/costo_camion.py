# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 23:00:26 2021

@author: Jony
"""

import informe_funciones
def costo_camion(nombre_archivo):
    costototal=0.0 #inicializamos un acumulador
    camion = informe_funciones.leer_camion(nombre_archivo)
    costototal += sum([s['cajones'] * s['precio'] for s in camion])
    return costototal

costo_camion('../Data/camion.csv')

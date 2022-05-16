# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 19:44:16 2021

@author: Jony
"""

def leer_precios(nombre_archivo):
    import csv # Lee la lista de precios de un archivo csv, devuelve un dictionary con el nombre de la fruta como key y el precio como value
    camion = {}
    with open(nombre_archivo, 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                camion[row[0]] = row[1]
            except IndexError:
                print ('Linea con datos faltantes')
        return camion

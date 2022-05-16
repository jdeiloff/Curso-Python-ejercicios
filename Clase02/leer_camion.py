# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 22:20:05 2021

@author: Jony
"""

def leer_camion(nombre_archivo):
    import csv # Devuelve un dictionary con keys fijas( nombre, cajones, precio) y saca las values desde un archivo csv.
    llaves = ['nombre', 'cajones', 'precio']
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote = (row[0], int(row[1]), float(row[2]))
            camion.append(lote)
        dcamion = [dict(zip(llaves, l)) for l in camion]
    return dcamion

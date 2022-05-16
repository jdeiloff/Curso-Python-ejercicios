# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 18:15:05 2021

@author: Jony
"""

def leer_camion(nombre_archivo):
    import csv # Devuelve una lista de dictionarrios y saca los valores desde un archivo csv.
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote = (row[0], int(row[1]), float(row[2]))
            camion.append(lote)
        dcamion = [dict(zip(headers, l)) for l in camion]
    return dcamion


def leer_precios(nombre_archivo):
    import csv # Lee la lista de precios de un archivo csv, devuelve un dictionary con el nombre de la fruta como key y el precio como value
    precios = {}
    with open(nombre_archivo, 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                precios[row[0]] = row[1]
            except IndexError:
                break
        return precios

carga_camion = leer_camion('../Data/camion.csv') # Lee el archivo camion.csv
precios_total = leer_precios('../Data/precios.csv') # Lee el archivo precios.csv
costo_camion = 0.0
recaudado = 0.0

for s in carga_camion:
    costo_camion += s['cajones'] * s['precio']   # Calcula el costo de la carga.
    recaudado += s['cajones'] * float(precios_total[s['nombre']]) # Calcula lo ganado en ventas.
diferencia = recaudado - costo_camion # Calcula la diferencia entre lo recaudado y el costo de la carga.

if diferencia > 0:                   # Indica si hubo ganancia o perdida en base a la diferencia.
    resultado = 'Hubo ganancia'
else:
    resultado = 'Hubo pérdida'
    
print(f'Costo de la carga: ${costo_camion} Recaudado: ${recaudado} Diferencia: ${round(diferencia, 2)}. {resultado}')

costo = sum([s['cajones']*s['precio'] for s in camion])

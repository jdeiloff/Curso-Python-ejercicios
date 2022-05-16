# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 00:16:56 2021

@author: Jony
"""

# ticker.py 10.10

from vigilante import vigilar
import csv
import informe_final
import formato_tabla

def elegir_columnas(rows, indices):
    for row in rows:
        yield (row[index] for index in indices)
        
def cambiar_tipo(rows, types):
    for row in rows:
        yield (func(val) for func, val in zip(types, row))

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

def filtrar_datos(rows, nombres):
    for row in rows:
        if row['nombre'] in nombres:
            yield row

def imprimir_vigilante(data_informe, formateador):           # Imprime el informe de precios desde una lista de tuplas.
    formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
    for nombre, precio, volumen in data_informe:
        rowdata = [nombre, precio, volumen]
        formateador.fila(rowdata)

def ticker(camion_file, log_file, fmt):
    camion = informe_final.leer_camion(camion_file)
    rows = parsear_datos(vigilar('../Data/mercadolog.csv'))
    rows = filtrar_datos(rows, camion)
    formateador = formato_tabla.crear_formateador(fmt)
    for row in rows:
        imprimir_vigilante(row, formateador)

'''
camion = informe_final.leer_camion('../Data/camion.csv')
rows = parsear_datos(vigilar('../Data/mercadolog.csv'))
rows = filtrar_datos(rows, camion)
for row in rows:
    print(row)
'''  
  
'''
if __name__ == '__main__':
    lines = vigilar('../Data/mercadolog.csv')
    rows = parsear_datos(lines)
    for row in rows:
        print(row)
        '''
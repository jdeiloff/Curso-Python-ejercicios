# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 23:19:40 2021

@author: Jony
"""
from collections import ChainMap
import csv 
    
def leer_camion(nombre_archivo): # Devuelve un list con s fijas( nombre, cajones, precio) y saca las values desde un archivo csv.
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote = (row[0], int(row[1]), float(row[2]))
            camion.append(lote)
        dcamion = [dict(zip(headers, l)) for l in camion]
    return dcamion


def leer_precios(nombre_archivo): # Lee la lista de precios de un archivo csv, devuelve un dictionary con el nombre de la fruta como  y el precio como value
    precios = {}
    with open(nombre_archivo, 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                precios[row[0]] = row[1]
            except IndexError:
                break
        return precios
    
def hacer_informe(lista_cajones, dict_precios):
    lista_tuplas = []
    for line in lista_cajones:
        tupla = (line['nombre'], line['cajones'], line['precio'], round((float(dict_precios[line['nombre']]) - float(line['precio'])), 2))
        lista_tuplas.append(tupla)
    return lista_tuplas

camion = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')
informe = hacer_informe(camion, precios)
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
        

print(f' {headers[0]:>9} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print('---------- ---------- ---------- ----------')

for linea in informe:
    precio_modificado = (f'${linea[2]}')
    cambio_modificado = (f'${round(linea[3], 2)}')
    print(f' {linea[0]:>9s} {(linea[1]):>10} {precio_modificado:>10s} {cambio_modificado:>10.2s}')
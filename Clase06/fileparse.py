# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 00:08:39 2021

@author: Jony
"""

# fileparse.py
import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

        # Lee los encabezados del archivo
        if has_headers == True:
            encabezados = next(filas)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios
            
        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []
        
        
        registros = []
        for fila in filas:
            if types:
                fila = [func(val) for func, val in zip(types, fila)]
            else:
                fila = []
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]

            # Armar el diccionario
            if has_headers == True:
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
            elif has_headers == False:
                registros.append(fila)

    return registros
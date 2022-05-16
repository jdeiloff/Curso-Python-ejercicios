# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 01:08:39 2021

@author: Jony
"""

import csv

def read_data(lines):
    records = []
    for line in lines:
        line = line + ''
        records.append(line)
    return records

def parse_csv(iterable, select = None, types = None, has_headers = True, silence_errors = False):
    '''
    Parsea un iterable en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    Se pueden silenciar los errores con 'silence_errors = True'.
'''

    try:
        filas = csv.reader(read_data(iterable))

        # Lee los encabezados del archivo
        if has_headers == True:
            encabezados = next(filas)
        if has_headers == False and not select == None:
            raise RuntimeError('Para seleccionar, necesito encabezados')
            
        ''' Si se indicó un selector de columnas,
            buscar los índices de las columnas especificadas.
        '''
            
        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []
        
        
        registros = []
        for line, fila in enumerate(filas):
            try:
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
            except ValueError as e:
                if silence_errors == False:
                    print(f'Fila {line}: No pude convertir {fila}.\nFila {line}: Motivo: {e}')
                continue
        return registros
    except RuntimeError as e:
        print(e)

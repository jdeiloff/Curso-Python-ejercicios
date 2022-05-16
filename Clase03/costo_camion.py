# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 22:49:46 2021

@author: viejo
"""

def costo_camion(nombre_archivo):
    "Recibe un nombre de archivo como entrada, lee la información sobre los cajones cargados en el camión y devuelve el costo de la carga como float"
    import informe_funciones
    try:
        total = 0
        
        rows = informe_funciones.leer_camion(nombre_archivo)
        for fila, line in enumerate(rows, start=1):
             try:
                 record = dict(zip(headers, line))
                 ncajones = int(record['cajones'])
                 precio = float(record['precio'])
                 total += ncajones * precio
             except ValueError:
                 print(f"Faltan datos de cajón o precio para {line[0]}, en la fila {fila}, tengo {line}")
        return total
    except FileNotFoundError:
        print(f'El archivo "{nombre_archivo}" no fue encontrado, intente nuevamente.')
    print("El costo total es $",total)
    
costo_camion('../Data/camion.csv')
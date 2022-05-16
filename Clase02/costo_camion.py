# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 18:58:17 2021

@author: Jony
"""

def costo_camion(nombre_archivo):
    "Recibe un nombre de archivo como entrada, lee la información sobre los cajones cargados en el camión y devuelve el costo de la carga como float"
    import csv
    total = 0
    f = open(nombre_archivo)
    rows = csv.reader(f)
    for line in rows:
        try:
            total += float(line[1])*float(line[2])
        except ValueError:
            print("Faltan datos de cajón o precio para",line[0])
    return total
    print("El costo total es $",total)
    f.close()

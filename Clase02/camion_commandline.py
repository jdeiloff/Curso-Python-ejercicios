# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 21:03:14 2021

@author: Jony
"""
import csv
import sys

def costo_camion(nombre_archivo):
    "Recibe un nombre de archivo como entrada, lee la información sobre los cajones cargados en el camión y devuelve el costo de la carga como float"
    costo = 0
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    if len(sys.argv) == 2:
        nombre_archivo = sys.argv[1]
    else:
        nombre_archivo = "../Data/camion.csv"
    for line in rows:
        try:
            costo += float(line[1])*float(line[2])
        except ValueError:
            print("Faltan datos de cajón o precio para",line[0])

    print("El costo total es $",costo)
    f.close()

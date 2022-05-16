# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 19:30:14 2021

@author: Jony
"""
def buscar_precio(fruta):
    "Busca y muestra como float el precio del cajón fruta buscada, si es que está"
    import csv
    with open("../Data/precios.csv", "rt") as f:
        for line in f:
            row = line.split(",")
            if fruta in row:
                print("El precio de un cajón de",fruta,"es: $",float(row[1]))
                break
        else:
            print(fruta,"no figura en el listado de precios.")

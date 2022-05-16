# -*- coding: utf-8 -*-

#!/usr/bin/env python3

"""
Created on Mon Sep 27 15:00:35 2021

@author: Jony
"""

import fileparse
import sys

def leer_camion(nombre_archivo):
    camion=fileparse.parse_csv(nombre_archivo, types=[str, int, float])
    return(camion)

def leer_precios(nombre_archivo):
    precios = fileparse.parse_csv(nombre_archivo,has_headers=False, types=[str, float])
    lista={}
    for line in precios:
        nombre=line[0]
        lista[nombre]=line[1]
    return(lista)

def hacer_informe(camion,precios):
    informe=[]
    for s in camion:
        nombre=s['nombre']
        cambio=precios[nombre]-s['precio']
        tupla=(nombre,s['cajones'],precios[nombre],cambio)
        informe.append(tupla)
    return(informe)


def imprimir_informe(informe):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    sep=('----------', '----------', '----------', '----------')
    for nombre, cajones, precio, cambio in [headers,sep]:
        print(f'{nombre:>10s} {cajones:>10s} {precio:>10s} {cambio:>10s}')
    for nombre, cajones, precio, cambio in informe:
        precio='$'+str(precio)
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')
    
def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion=camion=leer_camion(nombre_archivo_camion)
    precios=leer_precios(nombre_archivo_precios)
    informe=hacer_informe(camion,precios)
    return(imprimir_informe(informe))


def f_principal(argv):
    if len(argv)!=3:
        print('uso inadecuado, revisar argumentos.')
    else:
        camion=argv[1]
        precios=argv[2]
        informe_camion(camion,precios)
      
if __name__ == '__main__':
    f_principal(sys.argv)
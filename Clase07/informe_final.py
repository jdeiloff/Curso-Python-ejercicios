#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fileparse
import sys

def leer_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    with open(nombre_archivo) as file:
        camion = fileparse.parse_csv(file, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
        return camion

def leer_precios(nombre_archivo):
    with open(nombre_archivo) as file:
        precios = fileparse.parse_csv(file,has_headers=False, types=[str, float])
        lista={}
        for line in precios:
            nombre=line[0]
            lista[nombre]=line[1]
        return lista

def hacer_informe(camion, precios):
    lista = []
    for lote in camion:
        precio_venta = precios[lote['nombre']]
        cambio = precio_venta - lote['precio']
        t = (lote['nombre'], lote['cajones'], precio_venta, cambio)
        lista.append(t)
    return lista

def imprimir_informe(informe):           # Imprime el informe de precios
    print('    Nombre    Cajones     Precio     Cambio')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        precio = f'${precio}'
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')

def informe_camion(nombre_archivo_camion, nombre_archivo_precios): # Llama al resto de las funciones para generar el informe e imprimirlo.
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)
    
def f_principal(parametros): # Llama al resto de las funciones para generar el informe e imprimirlo.
    if len(parametros) != 3:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion archivo_precios')
    else:
        camion = parametros[1]
        precios = parametros[2]
        informe_camion(camion, precios)

if __name__ == '__main__':
    f_principal(sys.argv)
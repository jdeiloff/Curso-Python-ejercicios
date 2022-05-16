#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fileparse
import formato_tabla
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

def imprimir_informe(data_informe, formateador):           # Imprime el informe de precios desde una lista de tuplas.
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)

def informe_camion(archivo_camion, archivo_precios, fmt = 'txt'):
    '''
    Crea un informe por camion a partir de archivos camion y precio.
    '''
    # Leer archivos con datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    # Obtener los datos para un informe
    data_informe = hacer_informe(camion, precios)

    # Imprimir
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)
    
def f_principal(parametros): # Llama al resto de las funciones para generar el informe e imprimirlo.
    if len(parametros) < 3:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion archivo_precios formato(opcional)')
    else:
        camion = parametros[1]
        precios = parametros[2]
        fmt = parametros[3]
        informe_camion(camion, precios, fmt)

if __name__ == '__main__':
    f_principal(sys.argv)

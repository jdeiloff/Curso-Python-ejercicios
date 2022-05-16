# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 11:33:08 2021

@author: Jony
"""

# Ejercicio 3.18
import csv
from collections import Counter

def leer_parque(lista_arboles, parque):    # Toma un nombre de parque y devuelve todos los arboles de alli.
        lista = []
        with open(lista_arboles, 'rt', encoding="utf8") as f:
            filasarboles = csv.reader(f)
            headers = next(f)
            for datos in filasarboles:
                registro = dict(zip(headers, filasarboles))
                registro['altura_tot'] = float(registro['altura_tot'])  # Convierte en float las alturas para poder calcular.
                if parque.lower() in (datos[10]).lower():
                    lista.append(registro)
        return lista

def especies(lista_arboles):   # Devuelve lista de arboles
    lista = []
    for arbol in lista_arboles:
        lista.append(arbol['nombre_com'])
    return set(lista)

def contar_ejemplares(lista_arboles): # Cuenta los ejemplares de arboles de la lista.
    d = Counter()
    for arbol in lista_arboles:
        d[arbol['nombre_com']] += 1
    return d


    
def obtener_alturas(lista_arboles, especie): # Obtiene altura de la lista de arboles.
    lista = []
    for arbol in lista_arboles:
        if arbol['nombre_com']  == especie:
            lista.append(arbol['altura_tot'])
    return lista

def leer_arboles(nombre_archivo): # Devuelve lista con todos los datos de los arboles.
    arboleda = []
    registro = {}
    with open(nombre_archivo, 'rt', encoding="utf8") as f:
        arboles = csv.reader(f)
        headers = next(f).split(',')
        types =  [float, float, int, int, int, int, int, str,  # Paso TODOS los tipos de valores.
                 str, str, str, str, str, str, str, float, float]
        for datos in arboles:
            datosconv = [func(val) for func, val in zip(types, datos)]
            registro = dict(zip(headers, datosconv))
            arboleda.append(registro)
    return arboleda

def al_diam(arboleda, nombre_com): # Devuelve altura y diametro de un arbol (similar a 4.17)
    aldiam = [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == nombre_com]
    return aldiam

def medidas_de_especies(especies,arboleda): # Genera diccionario con la info de arbol en especies, NOTA TARDA MUCHISIMO<<<<<.
    medidas = {arbol['nombre_com']: al_diam(arboleda, arbol['nombre_com']) for arbol in especies if arbol['nombre_com'] in especies}
    return medidas


# Ejercicio 4.16 Altura Jacarandas
#arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
# H=[float(arbol['altura_tot']) for arbol in arboleda]
#aljacaranda = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
# Ejercicio 4.18 Altura y Diametro Jacaranda
#aldiamjacaranda = [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
#especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
#medidas = medidas_de_especies(especies,arboleda)

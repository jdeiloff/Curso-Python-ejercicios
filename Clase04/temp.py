# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
nombres = ['Edmundo', 'Juana']
import csv

def leer_arboles(nombre_archivo):
    arboleda = []
    with open(nombre_archivo, encoding="utf8") as f:
        filas = csv.reader(f)
        enc = next(f).split(',')
        tipos = [float, float, int, int, int, int, int, str,
                 str, str, str, str, str, str, str, float, float]
        for fila in filas:
            fila_tip = [func(val) for func, val in zip(tipos, fila)]
            record = {}
            record = dict(zip(enc, fila_tip))
            arboleda.append(record)
    return arboleda

def lista_alt_diam(arboleda, nombre):
    HD = [(arbol['altura_tot'], arbol['diametro'])
          for arbol in arboleda if arbol['nombre_com'] == nombre]
    return HD
def medidas_de_especies(especies, arboleda):
    diccionario = {arbol['nombre_com']: lista_alt_diam(
        arboleda, arbol['nombre_com']) for arbol in arboleda if arbol['nombre_com'] in especies}
    return diccionario

def main():
    # from pprint import pprint
    arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
    # H=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    # # print(H)
    # HD=[(arbol['altura_tot'],arbol['diametro']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    # pprint(HD)
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    dicc = medidas_de_especies(especies, arboleda)
    print(len(dicc['Eucalipto']))
    print(len(dicc['Palo borracho rosado']))
    print(len(dicc['Jacarandá']))
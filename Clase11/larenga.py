# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 15:44:02 2021

@author: Jony
"""

def pascal(n, k):
    """
    Toma un valor para la fila n y otro para la columna k,
    ambos deben ser enteros positivos y k debe ser al menos n+1
    para devolver un triangulo de Pascal, donde los valores de 
    cada fila se enumeran desde 0 (de izquierda a derecha). 
    Los valores que se encuentran en los bordes del triángulo 
    son todos 1. Cualquier otro valor se calcula sumando los 
    dos valores contiguos de la fila de arriba.
    """
    if k == 0:
        return 1
    if n == 0:
        return k
    return (n * pascal(n-1, k-1)) / k
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 22:36:00 2021

@author: Jony
"""

def fibonacci(n):
    """
    Toma un entero positivo n y
    devuelve el n-ésimo número de Fibonacci
    de forma recursiva
    utilizando un diccionario para almacenar los valores ya computados.
    dict_fibo es un diccionario que guarda en la clave 'k' el valor de F(k)
    donde F(0) = 0 y F(1) = 1.
    """
    dict_fibo = {0:0, 1:1}
    if n in dict_fibo:
        F = dict_fibo[n]
    dict_fibo[n] = fibonacci(n-1) + fibonacci(n-2)
    return F



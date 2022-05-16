# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 18:28:55 2021

@author: Jony
"""
''' valor_absoluto devuelve el valor modulo absoluto de un numero entero dado.
    pre = numero entero
    pos = numero entero sin signo (valor absoluto)
    inv = n ve si es mayor a cero, te devuelve el mismo numero, si es negativo, te devuelve el numero sin el signo.
'''
def valor_absoluto(n):
    if n >= 0:
        return n
    else:
        return -n
    
'''
    suma_pares devuelve la suma de numeros pares de un numero dado
    pre = numero par
    pos = suma de los numeros pares
    inv = res va probando si e es divisible por 2 (par), si lo es suma ese valor y si no lo es no lo suma
'''    
def suma_pares(l):
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res


def veces(a, b):
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res
'''
devuelve la suma de a, b veces (básicamente a*b)
pre = a debe ser cualquier entero, b un entero positivo
pos = devuelve a * b
inv = res va sumando a varias veces hasta llegar a b veces.
'''
def collatz(n):
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res

'''
Collatz pide un numero entero cualquiera, si es par, lo divide por 2. Si es impar lo multiplica por 3 y le suma 1.
pre = un numero entero cualquiera
pos = devuelve si es par, el numero dividio entero por 2, si no lo es lo multiplica por 3 y le suma 1.
inv = res va tomando los valores que vienen dados de las operaciones hechas a n.
'''
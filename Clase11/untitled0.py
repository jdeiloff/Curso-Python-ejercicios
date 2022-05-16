# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 19:49:29 2021

@author: Jony
"""
#Factorial Recursivo (eficiente) 
def factorial(n):
    if n == 1:
        r = 1
        return r

    f = factorial(n-1)
    r = n * f
    return r

#%% Factorial Iterativo (poco eficiente)
def factorial(n):
    """Precondición: n entero positivo
       Devuelve: n!"""
    fact = 1
    for num in range(n, 1, -1):
        fact *= num
    return fact

#%% Potencia Recursivo (Muy Eficiente)
def potencia(b,n):
    """Precondición: n >= 0
       Devuelve: b^n."""

    if n <= 0:
        # caso base
        return 1

    if n % 2 == 0:
        # caso n par
        p = potencia(b, n // 2)
        return p * p
    else:
        # caso n impar
        p = potencia(b, (n - 1) // 2)
        return p * p * b
    
#%% Potencia Iterativo (Poco eficiente)

def potencia(b, n):
    """Precondición: n >= 0
       Devuelve: b^n."""

    pila = []
    while n > 0:
        if n % 2 == 0:
            pila.append(True)
            n //= 2
        else:
            pila.append(False)
            n = (n - 1) // 2

    p = 1
    while pila:
        es_par = pila.pop()
        if es_par:
            p *= p
        else:
            p *= p * b

    return p

#%% Fibbonacci recursivo (poco eficiente)
def fib(n):
    """Precondición: n >= 0.
       Devuelve: el número de Fibonacci número n."""
    if n == 0:
        res = 0
    elif n == 1:
        res = 1
    else:
        res = fib(n - 1) + fib(n - 2)
    return res
#%% Fibbonacci iterativo
def fib(n):
    """Precondición: n >= 0.
       Devuelve: el número de Fibonacci número n."""
    if n == 0 or n == 1:
        return n
    ant2 = 0
    ant1 = 1
    for i in range(2, n + 1):
        fibn = ant1 + ant2
        ant2 = ant1
        ant1 = fibn
    return fibn
#%% sumar recursiva
def sumar(lista):
   """Devuelve la suma de los elementos en la lista."""
   '''
   caso base
   if len(lista) == 0:
    return 0
   '''
   res = 0
   if len(lista) != 0:
       res = lista[0] + sumar(lista[1:]) # Llamada recursiva sumar(lista[1:])
   return res
#%% recursividad de cola
def sumar(lista):
    """Devuelve la suma de los elementos en la lista."""
    suma = 0
    while lista:
        lista, suma = lista[1:], lista[0] + suma
    return suma
#%% funcion promediar con f interna no llamable y recursiva
"""Devuelve el promedio de los elementos de una lista de números."""

def promediar_aux(lista):
    suma = lista[0]
    cantidad = 1    
    if len(lista) > 1:
        suma_resto, cantidad_resto = promediar_aux(lista[1:])
        suma += suma_resto
        cantidad += cantidad_resto
    return suma, cantidad

suma, cantidad = promediar_aux(lista)
return suma / cantidad

#%% potencia con wrapper auxiliar que permite usar n negativos (requiere renombrar potencia recursiva a _potencia
def potencia(b, n):
    """Precondición: n es entero
       Devuelve: b^n."""
    if n < 0:
        b = 1 / b
        n = -n
    return _potencia(b, n))
#%%
print(len(str(2)))
def cant_digitos(n):
    cant = len(str(n))
    if cant == 0:
        return 
#%%
'''
Si yo quiero hacer una función que sume 1 hasta N de forma recursiva, una solución es:
    '''
def sumatoria(n):
    if n==1:
        return 1
    return n+sumatoria(n-1)

#%% otra
def sumatoria(n):
    i=1
    def aux(n,i):

        if i==n:
            return 1
        i=i+1
        return i+aux(n,i)
    return aux(n,i)
#%%
def es_potencia(n,b):
    #casos base
    if n == 1 and b == 0:
        return True
    if n == 1 and b != 0:
        return True
    else:
        if n % b == 0:
            return es_potencia(n//b, b)
    return False

#%%
def es_potencia(n, b):
    if n == 1:
        return True
    if n%b == 0:
        return es_potencia(n//b, b)
    else:
        return False
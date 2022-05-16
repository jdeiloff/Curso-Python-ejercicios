# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 18:04:09 2021

@author: Jony
"""

# Ejercicio 3.1. Semántica.

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            return False
        i += 1

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

# Al proponer el retorno de False en el condicional else y no al final del while, siempre va a devolver False si no empieza con la letra 'a', aunque la letra aparezca mas adelante en la cadena. Quite el else y coloque el retorno de False al final del while. No tiene en cuenta la 'A' (mayusculas), agregue el or 'A' en el while.
# En el bloque siguiente esta el codigo corregido
#%%

#Ejercicio 3.1 corregido.

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a' or 'A':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#%%

# Ejercicio 3.2. Sintaxis.

def tiene_a(expresion)
    n = len(expresion)
    i = 0
    while i<n
        if expresion[i] = 'a'
            return True
        i += 1
    return Falso

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

# Faltaban los dos puntos ':' luego de la declaracion de funcion, del while y del if (lineas 29, 32, 33). Para indicar si algo es igual a otra cosa se utiliza == y no =(linea 48). Falso no existe, el bool correcto es False en el siguiente bloque esta el codigo corregido (linea 36).
# No tenia en cuenta la 'a' mayuscula, solo la minuscula. (linea 48) A menos que sea la intencion del programa.

#%%

# Ejercicio 3.2 corregido.

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a' or 'A':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell') 

#%%

# Ejercicio 3.3. Tipos.
# En el tercer caso (1984) esta escrito como int, por lo que el programa da TypeError, para permitir que el programa ejecute correctamente esos casos, transformo la expresion en string con str() en las lines 79 y 83.
# Codigo corregido en el siguiente bloque.

def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)

#%%

# Ejercicio 3.3 corregido

def tiene_uno(expresion):
    n = len(str(expresion))
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if str(expresion)[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)

#%%

# Ejercicio 3.4. Alcances.
# En la definicion de la funcion, faltaba declarar que retorna esa funcion, al agregar al final de la declaracion de la funcion, return c, la aplicacion funciona como deberia.
# En el siguiente bloque esta el codigo corregido.

def suma(a,b):
    c = a + b

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%
# Ejercicio 3.4. Corregido.

def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%

# Ejercicio 3.5. Pisando memoria.
# Al generar el diccionario en el for, continuamente graba en el dict reteniendo el valor de la ultima fila en cada iteracion, para evitarlo, planteo formar el dict en registro, para evitar pisar en cada iteracion la misma posicion en la memoria.
# El codigo corregido esta en el siguiente bloque
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)

#%%

# Ejercicio 3.5. Corregido
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = {
                encabezado[0] : fila[0],
                encabezado[1] : int(fila[1]),
                encabezado[2] : float(fila[2])
                }
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)
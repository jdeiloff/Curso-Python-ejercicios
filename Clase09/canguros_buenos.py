# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 19:38:44 2021

@author: Jony

CanguroBueno, partes basadas en código visto de StackOverflow
para asignación de objetos.
"""

class Canguro:
    """
    Objeto canguro que es capaz de guardar dentro de su
    bolsa (marsupio) otros objetos, incluyendo otro 
    canguro.
    """

    def __init__(self, nombre, contenido = None):
        if contenido == None:
            contenido = []
        """
        Conviene asignar como valor predeterminado en clases 
        o funciones objetos inmutables y si son mutables,
        asignarlos como None e inicializarlas luego para evitar 
        arrastrar ese objeto como estuvo en la llamada anterior.
        """
        self.nombre = nombre
        self.contenido_marsupio = contenido

    def __str__(self):
        i = [ self.nombre + ' tiene en la bolsa:' ]
        for item in self.contenido_marsupio:
            c = ' ' + str(item)
            i.append(c)
        return '\n'.join(map(str,i))

    def meter_en_marsupio(self, item): # Agrega objeto a la bolsa del canguro.
        self.contenido_marsupio.append(item)

#%%
"""
canguromalo

Este código continene un 
bug importante y dificil de ver 
CORREGIDO GRACIAS A CANDID MOE EN STACKOVERFLOW
"""

class Canguro:
    """Un Canguro es un marsupial.

    """

    def __init__(self, nombre, contenido = None):
        if contenido == None:
            contenido = []
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        
        Conviene asignar como valor predeterminado en clases 
        o funciones objetos inmutables y si son mutables,
        asignarlos como None e inicializarlas luego para evitar 
        arrastrar ese objeto como estuvo en la llamada anterior.
        """
        self.nombre = nombre
        self.contenido_marsupio = contenido

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)


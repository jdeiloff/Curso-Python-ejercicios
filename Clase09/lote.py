# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 14:56:31 2021

@author: Jony
"""

class Lote:
    def __init__(self, f, c, p):
        # Todo dato guardado en `self` es propio de esa instancia
        self.nombre = f
        self.cajones = c
        self.precio = p
    
    def __str__(self):
        return f'Lote: {repr(self.nombre)} / {self.cajones} / ${self.precio}'
    
    def __repr__(self):
        return f'Lote({self.nombre}, {self.cajones}, {self.precio})'
        
    def costo(self):
        return self.cajones * self.precio
    
    def vender(self, n):
        self.cajones -= n 

class Lote_inf(Lote):
    def costo(self):
        return 1.25 * self.cajones * self.precio

milote = Lote_inf('Pera', 100, 10)
print(milote.costo())

class MiLote(Lote):
    def rematar(self):
        self.vender(self.cajones)
    def costo(self):
        return 1.25 * self.cajones * self.precio

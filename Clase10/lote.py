# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 14:56:31 2021

@author: Jony
"""

class Lote:
    def __init__(self, nombre, cajones, precio):
        # Todo dato guardado en `self` es propio de esa instancia
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
    
    def __str__(self):
        return f'{self.nombre}-{self.cajones}-{self.precio}'
    
    def __repr__(self):
        return f'Lote({self.nombre}, {self.cajones}, {self.precio})'
        
    def costo(self):
        return self.cajones * self.precio
    
    def vender(self, unidades):
        self.cajones -= unidades 


class MiLote(Lote):
    def rematar(self):
        self.vender(self.cajones)
    def costo(self):
        return 1.25 * self.cajones * self.precio

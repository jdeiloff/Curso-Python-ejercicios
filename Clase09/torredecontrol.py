# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 14:35:16 2021

@author: Jony
"""

class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0

class Aire(Cola):
    def __init__(self):
        super().__init__()
        
    def nuevo_arribo_sup(self,vuelo):
        self.encolar(vuelo)
               
    def asignar_pista_v(self):
        if self.esta_vacia():
            return('No hat vuelos en espera.')
        print(f'El vuelo {self.items[0]} aterrizó con éxito.')
        self.desencolar()

class Tierra(Cola):
    def __init__(self):
        super().__init__()
            
    def nueva_partida_sup(self,vuelo):
        self.encolar(vuelo)
        
    def asignar_pista_t(self): 
        if self.esta_vacia():
            return('No hay vuelos en espera.')
        print(f'El vuelo {self.items[0]} despegó con éxito.')
        self.desencolar()
            
class TorreDeControl (Aire, Tierra):
    def __init__(self):
        self.torre_control = Aire()
        self.Tierra = Tierra()
    
    def nuevo_arribo(self,vuelo):
        self.torre_control.nuevo_arribo_sup(vuelo)
        
    def nueva_partida(self,vuelo):
        self.Tierra.nueva_partida_sup(vuelo)
    
    def ver_estado(self):
        print(f'Vuelos esperando para despegar: {", ".join(self.Tierra)}')
        print(f'Vuelos esperando para aterrizar: {", ".join(self.torre_control)}')
    
    def asignar_pista(self):
        self.torre_control.asignar_pista_v
        self.Tierra.asignar_pista_t
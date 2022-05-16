# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 14:46:07 2021

@author: Jony
"""

class Camion:
    def __init__(self, lotes):
       self.lotes = lotes

    def __iter__(self):
        return self.lotes.__iter__()

    def __contains__(self, nombre):
        return any(lote.nombre == nombre for lote in self.lotes)
    
    def __len__(self):
        return len(self.lotes)
    
    def precio_total(self):
       return sum(l.costo() for l in self.lotes)

    def __getitem__(self,a):
        return self.lotes.__getitem__(a)
    
    def __repr__(self):
        return f'{self.lotes}'
    
    def __str__(self):
        camion = self.lotes.__iter__()
        for item in camion:
            c = ' ' + str(item)
            item.append(c)
        return '\n'.join(map(str,item))

    def contar_cajones(self):
       from collections import Counter
       cantidad_total = Counter()
       for l in self.lotes:
           cantidad_total[l.nombre] += l.cajones
       return cantidad_total
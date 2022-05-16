# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 15:31:41 2021

@author: Jony
"""

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expression[i] == 'a':
            return True
        else:
            return False
        i += 1
        
rta= tiene_a ('palabra')
print(rta)
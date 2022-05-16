# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 14:44:25 2021

@author: Jony
"""
'''
Le das dos cadenas, a y b, te devuelve una lista con
las posiciones donde b está dentro de a
'''
def posiciones_de(a,b):
    if len(b) > len(a):
        return []
    
    return posiciones_de(a[:-1], b) + (a[-len(b):] == b)*[len(a)-len(b)]
#%%
posiciones_de('Un tete a tete con Tete', 'te')
posiciones_de('Lololol lo lol', 'lo')
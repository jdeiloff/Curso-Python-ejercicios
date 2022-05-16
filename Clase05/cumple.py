# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 19:21:30 2021

@author: Jony
"""

# 5.3 Micumpleaños ('inspirado' en el artículo de Página 12 de Alan Paenza 'La Simulación de Monte Carlo')
import random

def cumple():
    
    dias = []
    for i in range(30):
        dias.append(random.randint(1,365))
    return dias


def probcumple(N):
    N=int(N)
    cumpleaños=cumple()
    G = sum([any(cumple().count(dia) > 1 for dia in cumple()) for i in range(N)])
    prob = float(G/N)
    return prob

probcumple(1)

#%%
from collections import Counter
 
def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]
   
List = [2, 1, 2, 2, 1, 3]
print(most_frequent(List))
#%%
a_list = [1, 2, 1]
List with duplicates


contains_duplicates = any(a_list.count(element) > 1 for element in a_list
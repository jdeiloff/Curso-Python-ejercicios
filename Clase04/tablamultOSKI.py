# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 12:44:59 2021

@author: Oski
"""

def tabla(N):
    print('  ',end='')
    for i in range(N):
        print(f'{i:>5d}', end='')
    print('')
    print('-'*54)
        
    for i in range(N):
       print(i, end='| ')
       s = 0
       for j in range(N):
           print(f'{s:>4d}', end=' ')
           s += i  
    
       print(' ')
       
tabla(10)
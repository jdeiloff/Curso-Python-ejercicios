# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 15:27:45 2021

@author: Jony
"""

#%%
cache = {0: 0, 1: 1}
[fibonacci_of(n) for n in range(15)]

def fibonacci_of(n):
     if n in cache:  # Base case
         return cache[n]
     # Compute and cache the Fibonacci number
     cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case
     return cache[n]
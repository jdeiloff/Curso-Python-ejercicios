# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 14:21:40 2021

@author: Jony
"""
import numpy as np
import matplotlib.pyplot as plt

def plotear_temperaturas():
    temperaturas = np.load('temperaturas.npy')
    return plt.hist(temperaturas,bins=70)

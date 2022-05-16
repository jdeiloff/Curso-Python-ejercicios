# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 16:08:23 2021

@author: Jony

Si le das un directorio en forma de string, te devuelve una lista 
con todos los archivos .png de ese directorio y de sus subdirectorios.

"""

import os
import sys


def archivos_png(directorio):
    lst=[]
    for root, dirs, files in os.walk(directorio): # Recorro subdirectorios y archivos
        lst += [os.path.join(root, file)for file in files if '.png' in file]       
    return lst
   

if __name__ == '__main__':
    archivos_png(sys.argv)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 15:09:37 2021

@author: Jony
"""

from datetime import datetime, timedelta
import sys

'''
La función requiere que le pases tu fecha de nacimiento
como una cadena (string) en formato dd/mm/AAAA (dia, 
mes, año con 2, 2 y 4 dígitos separados con barras
normales) y devuelve la vida en segundos como float.
'''

def vida_en_segundos(fecha_nac):
    nacimiento = datetime.strptime(fecha_nac, '%d/%m/%Y')
    hoy = datetime.now()
    vida = timedelta.total_seconds(hoy - nacimiento)
    return vida


if __name__ == '__main__':
    vida_en_segundos(sys.argv)


# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 15:43:39 2021

@author: Jony
"""

from datetime import datetime, timedelta


'''
La función requiere que le pases tu fecha de nacimiento
como una cadena (string) en formato dd/mm/AAAA (dia, 
mes, año con 2, 2 y 4 dígitos separados con barras
normales) y devuelve la vida en segundos como float.
'''

def dias_para_primavera():
    primavera = datetime.strptime('09-21-22', '%m-%d-%y')
    hoy = datetime.now()
    dias_spring = datetime(primavera - hoy)
    print(f'Faltan {dias_spring.day} días para la primavera 2022')
    return dias_spring
    

if __name__ == '__main__':
    dias_para_primavera()

# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 11:19:12 2021

@author: Jony
"""

import pandas as pd
import os

directorio = '../Data'
archivo1 = 'arbolado-en-espacios-verdes.csv'
archivo2 = 'arbolado-publico-lineal-2017-2018.csv'
e_verdes = os.path.join(directorio,archivo1)
lineal = os.path.join(directorio,archivo2)
df_parques = pd.read_csv(e_verdes)
df_veredas = pd.read_csv(lineal)
tipas = ['Tipuana tipu', 'Tipuana Tipu']
df_tipas_parques =  df_parques[df_parques['nombre_cie'].isin(tipas)].copy()
df_tipas_parques = df_tipas_parques.assign(ambiente = 'parque')
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'].isin(tipas)].copy()
df_tipas_veredas = df_tipas_veredas.rename(columns={'diametro_altura_pecho': 'diametro', 'altura_arbol': 'altura_tot'})
df_tipas_veredas = df_tipas_veredas.assign(ambiente = 'vereda')
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
df_tipas.boxplot('diametro',by = 'ambiente')
df_tipas.boxplot('altura_tot',by = 'ambiente')

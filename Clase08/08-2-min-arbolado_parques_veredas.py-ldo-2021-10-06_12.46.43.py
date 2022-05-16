# Ejercicio 8.9: Comparando especies en parques y en veredas
"""
Created on Tue Oct  5 18:53:57 2021

@author: ldominguez@inti.gob.ar
"""

import pandas as pd
import os

#1.Creamos datasets de ambos archivos
directorio = '../Data'
archivo_parques = 'arbolado-en-espacios-verdes.csv'
archivo_veredas = 'arbolado-publico-lineal-2017-2018.csv'
fname_parques = os.path.join(directorio,archivo_parques)
fname_veredas = os.path.join(directorio,archivo_veredas)
df_parques= pd.read_csv(fname_parques)
df_veredas= pd.read_csv(fname_veredas)

#2.Creamos sub-datasets con filas(TIpuana tipu) y 
# columnas seleccionadas(Altura, diametro)
cols_parques = ['altura_tot', 'diametro']
df_tipas_parques = df_parques[df_parques['nombre_cie'] == 
                              'Tipuana Tipu'][cols_parques].copy()
cols_veredas = ['altura_arbol', 'diametro_altura_pecho']
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == 
                              'Tipuana tipu'][cols_veredas].copy()

#renombramos altura y diametro en parques para que queden 
# homogeneizados ambos datasets
df_tipas_parques=df_tipas_parques.rename(columns={"altura_tot": "altura_arbol", "diametro": "diametro_altura_pecho"})

#3. Agregamos a cada dataframe una columna llamada 'ambiente' que en un caso 
# valga siempre 'parque' y en el otro caso 'vereda'.
long_parques=len(df_tipas_parques)
nueva_col='ambiente'
nueva_fil_parques=['parque']*long_parques
df_tipas_parques[nueva_col]=nueva_fil_parques

long_veredas=len(df_tipas_veredas)
nueva_fil_veredas=['vereda']*long_veredas
df_tipas_veredas[nueva_col]=nueva_fil_veredas

# 4.Juntamos ambos datasets.
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

# 5.Creamos un boxplot para los diámetros a la altura del pecho de la tipas 
# distinguiendo los ambientes
df_tipas.boxplot('diametro_altura_pecho', by = 'ambiente')

# 6.Creamos un boxplot para las alturas de la tipas distinguiendo los ambientes
df_tipas.boxplot('altura_arbol', by = 'ambiente')
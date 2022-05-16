# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 19:30:17 2021

@author: Jony
"""

import pandas as pd

df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col=['Time'], parse_dates=True)
df['12-25-2014':].plot()
df['10-15-2014':'12-15-2014'].plot()
dh = df['12-25-2014':].copy()
delta_t = -1 # tiempo que tarda la marea entre ambos puertos
delta_h = (dh['H_SF'].mean()-dh['H_BA'].mean()) # diferencia de los ceros de escala entre ambos puertos
pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 15:08:51 2021

@author: Jony
"""
import numpy as np
#%%ejercicio 11.16
np.random.seed(3141)
N=50
indep_vars = np.random.uniform(size = N, low = 0, high = 10)
r = np.random.normal(size = N, loc = 0.0, scale = 8.0)
dep_vars = 2 + 3 * indep_vars + 2*indep_vars**2 + r

#%%
x = indep_vars
xc = x**2
y = dep_vars
X = np.concatenate((x.reshape(-1,1),xc.reshape(-1,1)),axis=1)
X.shape
#%%
ajuste_lineal = linear_model.LinearRegression()
ajuste_lineal.fit(x.reshape(-1,1),y)

ajuste_lineal_xc = linear_model.LinearRegression()
ajuste_lineal_xc.fit(xc.reshape(-1,1),y)

ajuste_mult = linear_model.LinearRegression()
ajuste_mult.fit(x,y)

grilla_x = np.linspace(0, 10, 500)
grilla_ajuste_lineal = ajuste_lineal.predict(grilla_x.reshape(-1, 1))
grilla_ajuste_lineal_xc = ajuste_lineal_xc.predict(grilla_x**2).reshape(-1, 1)

grilla_doble = np.concatenate((grilla_x.reshape(-1,1,(grilla_x**2).reshape(-1,1))))
grilla_ajuste_mult = ajuste_mult.predict(grilla_doble)

#%%
plt.figure(figsize = [7,7])
plt.scatter(indep_vars, dep_vars)
plt.plot(grilla_x. grilla_ajuste_lineal, c = 'green', label = r'ajuste lineal')


#%% 11.17
def pot(x,n):
    X=x.reshape(-1,1)
    for i in range(n-1):
        X=np.concatenate((X**(i+2)).reshape(-1,1), axis=1)
        
#%%
for n in range(1,9):
    X = pot(x,n)
    ajuste_lineal = linear_model.LinearRegression()
    ajuste_lineal.fit(X,y)
    errores_lineal = y - ajuste_lineal.predict(X)
    ecm = (errores_lineal**2).mean()
    aic = AIC(y.shape[0], ecm, n+1)
    aices.append(aic)
    
grado = np.argmin(aices) +1
grado
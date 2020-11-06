#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 17:17:35 2020

@author: luis plazas y laura restrepo
"""

import matplotlib.pyplot as plt
from time import process_time

def funcion(x,y):
    #El usuario cambia el valor de esta variable
    ecuacion = 6-2*(y/x)
    return ecuacion


#El usuario cambia el valor de estas 4 variables
x_inicial = 1
x_final = 10
y_inicial = 5
tamanio_paso = 0.5

eje_x = [x_inicial]
eje_y = [y_inicial]
pos = 1
tiempo_inicial = process_time()

while eje_x[-1] < x_final:
    x = eje_x[pos-1] + tamanio_paso
    y = eje_y[pos-1] + funcion(eje_x[pos-1],eje_y[pos-1])*tamanio_paso
    eje_x.append(x)
    eje_y.append(y)
    pos += 1
    
plt.plot(eje_x,eje_y)

tiempo_final = process_time()
tiempo = tiempo_final-tiempo_inicial

print("\nTiempo de ejecución: " + str(tiempo))
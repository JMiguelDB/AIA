# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 19:48:11 2017

@author: JM
"""

import csv
import numpy as np

with open('No-show-Issue-Comma-300k.csv', 'r+') as f:
    reader = csv.reader(f)
    dataset = list(reader)

#Resultados de las pruebas
test = np.array(dataset)[1:,5]
#Datos de pruebas sin la columna de resultados
dataset = np.array(dataset)[1:]
dataset = np.delete(dataset,5,1)


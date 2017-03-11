# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 19:14:02 2017

@author: JM
"""

from clasificacion import clasificacion
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression

clasificacion = clasificacion()
clasificacion.caracteristicas([2, 10, 11])
clasificacion.validacion_cruzada(SGDClassifier(), 5)


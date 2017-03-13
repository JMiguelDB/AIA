# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 19:14:02 2017

@author: JM
"""

from clasificacion import clasificacion
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

#Las caracteristicas van de [0,11] ya que se han eliminado las columnas de fecha y la de asistencia
print("--------------- Clasificacion lineal -----------------")
clasificacion1 = clasificacion()
clasificacion1.representacion_grafica(10,11,"SMS","Dias de espera")
"""
#clasificacion1.caracteristicas([2, 10, 11])
clasificacion1.train(SGDClassifier())
clasificacion1.validacion_cruzada(SGDClassifier(), 5)

print("\n --------------- Clasificacion probabilistica ----------------- \n")
clasificacion2 = clasificacion()
#clasificacion2.caracteristicas([2, 10, 11])
clasificacion2.train(LogisticRegression())
clasificacion2.validacion_cruzada(LogisticRegression(), 5)

print("\n --------------- Arbol de decision ----------------- \n")
clasificador = DecisionTreeClassifier(criterion='entropy',max_depth=3,min_samples_leaf=5)
clasificacion3 = clasificacion()
#clasificacion3.caracteristicas([2, 10, 11])
clasificacion3.train(clasificador)
clasificacion3.validacion_cruzada(clasificador, 5)
"""

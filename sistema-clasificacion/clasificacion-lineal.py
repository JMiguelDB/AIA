# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 19:48:11 2017

@author: JM
"""

import csv
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDClassifier
import sklearn.metrics

def dayToNumber(day):
    if day == 'Monday': 
        return 0
    if day == 'Tuesday': 
        return 1
    if day == 'Wednesday': 
        return 2
    if day == 'Thursday': 
        return 3
    if day == 'Friday': 
        return 4
    if day == 'Saturday': 
        return 5
    if day == 'Sunday': 
        return 6
#----------- Cargamos los datos -----------------------------------------
with open('No-show-Issue-Comma-300k.csv', 'r+') as f:
    reader = csv.reader(f)
    dataset = np.array(list(reader))

#Conjunto de prueba
test = dataset[1:,5]
for i in range(len(test)):
    if test[i] == "No-Show":
        test[i] = 0
    else:
        test[i] = 1

#Conjunto de entrenamiento
dataset = dataset[1:]
dataset = np.delete(dataset,5,1)
dataset = np.delete(dataset,[2,3],1)
#Convertimos el string del dia a un numero y los dias de espera los convertimos a positivo
for i in range(len(dataset)):
    dataset[i][2] = dayToNumber(dataset[i][2])
    dataset[i][11] = abs(int(dataset[i][11]))
    if dataset[i][1] == "M":
        dataset[i][1] = 1
    else:
        dataset[i][1] = 0

dataset = dataset.astype(float)
#--- Escogemos las características que utilizaremos en el entrenamiento -------

#Escogemos las caracteristicas: Dia, SMS y dias de espera entre la llamada y el dia de la cita
x_dataset = dataset[:,[2, 10, 11]]

#----- Generamos el conjunto de prueba y de entrenamiento -----------------------
X_train, X_test, y_train, y_test = train_test_split(x_dataset,test,test_size = 0.25)

#----- Normalizamos los valores ya que los valores de las caracteristicas son muy diferentes ------

normalizador = StandardScaler().fit(X_train)
Xn_train = normalizador.transform(X_train)

normalizador = StandardScaler().fit(X_test)
Xn_test = normalizador.transform(X_test)

#------ Creamos el sistema de clasificacion -----------------------
clasificador = SGDClassifier().fit(X_train,y_train)

y_test_pred = clasificador.predict(X_test)

sklearn.metrics.accuracy_score(y_test,y_test_pred)

print(sklearn.metrics.classification_report(y_test,y_test_pred))



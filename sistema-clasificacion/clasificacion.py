# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 19:48:11 2017

@author: JM
"""

import csv
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import KFold
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import cross_val_predict
from sklearn.tree import export_graphviz
import scipy
import sklearn.metrics


class clasificacion():
    def __init__(self):
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
                          
        #Eliminamos las columnas de fechas, status y titulo de columna
        dataset = np.delete(dataset,[2,3,5],1)
        self.x_names = dataset[0]
        dataset = dataset[1:]
        #Convertimos el string del dia a un numero y los dias de espera los convertimos a positivo
        for i in range(len(dataset)):
            dataset[i][2] = self.__dayToNumber(dataset[i][2])
            dataset[i][11] = abs(int(dataset[i][11]))
            if dataset[i][1] == "M":
                dataset[i][1] = 1
            else:
                dataset[i][1] = 0
        
        self.x_data = dataset.astype(float)
        self.y_data = test.astype(float)
    

    def __dayToNumber(self,day):
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
   
    """
    Metodo que permite seleccionar las caracteristicas que seran utilizadas para la clasificacion.
    Recibe un numero o una lista de numeros.
    """
    def caracteristicas(self,car):
        self.x_data = self.x_data[:,car]
    
    """
    Metodo que genera el conjunto de prueba y de entrenamiento, y lo aplica al clasificador
    Recibe como parametro la velocidad de aprendizaje y el clasificador
    """
    def train(self,clasificador,learning_rate = 0.25):
        X_train, X_test, y_train, y_test = train_test_split(self.x_data,self.y_data,test_size = learning_rate)

        clasificador = clasificador.fit(X_train.astype(float),y_train.astype(float))
        y_test_pred = clasificador.predict(X_test.astype(float))
     
        print("\n -------------------------- Resultados clasificacion ----------------- \n")
        print("Precision del clasificador para el conjunto de pruebas:", sklearn.metrics.accuracy_score(y_test.astype(float),y_test_pred.astype(float)))
        print("Tasa de aciertos/fallos: \n",sklearn.metrics.confusion_matrix(y_test.astype(float),y_test_pred.astype(float)))
        print("Resumen: \n",sklearn.metrics.classification_report(y_test.astype(float),y_test_pred.astype(float)))

    """
    Metodo que aplica la validacion cruzada al tipo de clasificador pasado por parametros
    y diviendo el conjunto de datos en k trozos
    """
    def validacion_cruzada(self, clasificador, k, tipo):
        #Se genera un modelo que normaliza los datos y utiliza el clasificador recibido
        modelo = Pipeline([('normalizador', StandardScaler()), ('modelo', clasificador)])
        #Genera conjuntos de datos de tamaño k
        kfold = KFold(self.x_data.shape[0], k, shuffle = True)
        #Se realiza la valoración cruzada sobre el conjunto de datos
        valores = cross_val_score(modelo, self.x_data.astype(float), self.y_data.astype(float), cv=kfold)
        #Se predicen los valores a partir del conjunto de prueba
        predicted = cross_val_predict(modelo, self.x_data.astype(float), self.y_data.astype(float), cv=kfold)
        
        print("\n -------------------------- Resultados validacion cruzada ----------------- \n")
        print("Valoraciones obtenidas en el clasificador:", valores)
        print("Media de las valoraciones:", np.mean(valores))
        print("Error estandar:", scipy.stats.sem(valores))
        print("Precision del clasificador para el conjunto de pruebas:", sklearn.metrics.accuracy_score(self.y_data.astype(float),predicted.astype(float)))
        print("Tasa de aciertos/fallos: \n",sklearn.metrics.confusion_matrix(self.y_data.astype(float),predicted.astype(float)))
        print("Resumen: \n",sklearn.metrics.classification_report(self.y_data.astype(float),predicted.astype(float)))
        if tipo == "T":
            export_graphviz(clasificador,feature_names=self.x_names,out_file="test.dot")
        
    def representacion_grafica(self,x,y,x_name,y_name):
        for tipo,marca,color in zip(range(2),"soD","rgb"):
            plt.scatter(self.x_data[:,x][self.y_data == tipo],self.x_data[:,y][self.y_data == tipo],marker=marca,c=color)
        plt.xlabel(x_name)
        plt.ylabel(y_name)
        plt.show()

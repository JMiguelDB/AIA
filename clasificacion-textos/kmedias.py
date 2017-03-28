# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 19:25:15 2017

@author: JM
"""
from random import randint
from math import sqrt
from sklearn.datasets import load_iris
import numpy as np

class kmedias():
    def __init__(self,k,conj,dist_type):
        self.k = k
        self.conj = conj
        self.dist_type = dist_type
        
    def ejecuta(self):
        k = self.k
        conj = self.conj
        dist_type = self.dist_type
        #Obtenemos el tamaño de los elementos
        N = len(conj)-1
        #Inicializamos los centroides aleatoriamente
        #Falla si los centroides calculados aleatoriamente obtienen el mismo valor
        m = [conj[randint(0,N)] for i in range(k)]
        m_aplana = m.copy()
        m_ant = []
        i = 0
        print("Valores centroide iniciales", m)
        while m_aplana != m_ant:
            #Generamos el valor m de la iteracion anterior y creamos la lista que albergara el cluster de cada centroide
            m_ant = m.copy()
            clusters = [[] for _ in range(k)]
            #Recorremos todos los elementos y calculamos la distancia que hay entre ese elemento y todos los centroides
            for j in range(N):
                min_dist = 100
                cent = None
                for i in range(k):
                    if dist_type == "euclidea":
                        dist = kmedias.euclidea(conj[j],m[i])
                    elif dist_type == "manhattan":
                        dist = kmedias.manhattan(conj[j],m[i])
                    elif dist_type == "hamming":
                        dist = kmedias.hamming(conj[j],m[i])
                    #Almacenamos el centroide más cercano al valor y lo almacenamos en el cluster asociado al centroide
                    if dist < min_dist:
                        min_dist = dist
                        cent = i
                clusters[cent].append(conj[j])
            #print(clusters)
            #Calculamos la media de todos los valores de cada cluster que seran los nuevos valores de los centroides
            for i in range(k):
                m[i] = kmedias.media(clusters[i]) 
            #Comprobamos si los centroides son bidimensionales
            if all(isinstance(elem, np.ndarray) for elem in m):
                m_aplana = [x for sublist in m for x in sublist] 
                m_ant = [x for sublist in m_ant for x in sublist]
            else:
                m_aplana = m.copy()
            i += 1

        #Mostramos los valores resultantes obtenidos del algoritmo
        for n in range(len(clusters)):
            print("Tamaño del cluster con centroide en {}:".format(m[n]),len(clusters[n]))
            print("Cluster asociado al centroide {}:".format(m[n]), clusters[n])
        print("Num iteraciones",i)

        return m
    
    #Calcula la media de todos los elementos del cluster
    def media(elements):
        return sum(elements)/len(elements)
    
    """
    Calcula la distancia euclidea y para ello recibe como parametros un elemento y un centroide
    """
    def euclidea(x,y):
        dis = (x-y)**2
        if isinstance(dis,np.ndarray):
            dis = sum(dis)
        return sqrt(dis)
    """
    Calcula la distancia manhattan y para ello recibe como parametros un elemento y un centroide
    """
    def manhattan(x,y):
        dis = abs(x-y)
        if isinstance(dis,np.ndarray):
            dis = sum(dis)
        return dis
    """
    Calcula la distancia hamming y para ello recibe como parametros un elemento y un centroide
    """
    def hamming(x,y):
        dis = 0
        if isinstance(x,np.ndarray):
            for n in range(len(x)):
                if x[n] != y[n]:
                    dis += 1
        else:
            if x-y != 0:
                dis = 1
        return dis
    
    #Carga un conjunto de datos del tema de teoría.          
    def test():
        conj = [51, 43, 62, 64, 45, 42, 46, 45, 45, 62, 47, 52, 64, 51, 65, 48, 49, 46, 64, 51, 52, 62, 49, 
                     48, 62, 43, 40, 48, 64, 51, 63, 43, 65, 66, 65, 46, 39, 62, 64, 52, 63, 64, 48, 64, 48, 51, 
                     48, 64, 42, 48, 41]
        return conj
    
    """
    Carga el ejemplo de plantas visto en teoría.
    Recibe un número o lista correspondiente a las características que se utiizaran 
    """
    def iris_test(car):
        iris = load_iris()
        return iris.data[:,car]
        
print("\n --------------- Clasificacion ejemplo de teoria ----------------- \n")
test = kmedias(2,kmedias.test(),"manhattan")
print("Centroides obtenidos:",test.ejecuta())
"""
print("\n --------------- Clasificacion plantas ----------------- \n")
test1 = kmedias(3,kmedias.iris_test([2,3]),"euclidea")
print("Centroides obtenidos:",test1.ejecuta())
"""
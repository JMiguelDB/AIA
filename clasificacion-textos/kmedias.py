# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 19:25:15 2017

@author: JM
"""
from random import randint
from math import sqrt
from sklearn.datasets import load_iris

class kmedias():
    def __init__(self,k,conj,dist):
        self.k = k
        self.conj = conj
        self.dist = dist
        
    def ejecuta(self):
        k = self.k
        conj = self.conj
        dist = self.dist
        #Obtenemos el tamaño de los elementos
        N = len(conj)-1
        #Inicializamos los centroides aleatoriamente
        #Falla si los centroides calculados aleatoriamente obtienen el mismo valor
        m = [conj[randint(0,N)] for _ in range(k)] 
        m_ant = None
        print("Valores centroide", m)
        while m != m_ant:
            m_ant = m.copy()
            clusters = [[] for _ in range(k)]
            for j in range(N):
                min_dist = 100
                cent = None
                for i in range(k):
                    dist = kmedias.euclidea(conj[j],m[i])
                    if dist < min_dist:
                        min_dist = dist
                        cent = i
                    #print("Distancia", dist,"Valor",conj[j],"Centroide",m[i], "Valor centroide", cent)
                clusters[cent].append(conj[j])
            print("Clusters",clusters)
            for i in range(k):
                m[i] = kmedias.media(clusters[i])            
        return m
    
    def media(elements):
        val = 0
        print("Elements", elements)
        if all(isinstance(elem, list) for elem in elements):
            elements = [x for sublist in elements for x in sublist]
            val = sum(elements)/len(elements)       
        else:
            val = sum([elem for elem in elements])
            val = val / len(elements)
        return val
    def euclidea(x,y):
        print(x,y)
        dis = 0
        if isinstance(x, list) and isinstance(y, list):
            print("entra")
            for j in range(len(x)):
                dis += (x[j]-y[j])**2
        else:
            print("entra sin lista")
            dis = (x-y)**2
        print(sum(dis))####Quitar todo porque las listas se pueden restar directamente
        return sqrt(dis)
    #Carga un conjunto de datos del tema de teoría.          
    def test():
        conj = [51, 43, 62, 64, 45, 42, 46, 45, 45, 62, 47, 52, 64, 51, 65, 48, 49, 46, 64, 51, 52, 62, 49, 
                     48, 62, 43, 40, 48, 64, 51, 63, 43, 65, 66, 65, 46, 39, 62, 64, 52, 63, 64, 48, 64, 48, 51, 
                     48, 64, 42, 48, 41]
        return conj
        
    def iris_test():
        iris = load_iris()
        return iris.data
        
prueba = [[2,3],[3,4],[4,5]]
test = kmedias(2,kmedias.iris_test(),3)
print(test.ejecuta())
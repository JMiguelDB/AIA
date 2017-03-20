# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 19:25:15 2017

@author: JM
"""
from random import randint
from math import sqrt
import numpy as np

class kmedias():
    def __init__(self,k,conj,dist):
        #Obtenemos el tamaño de los elementos
        N = len(conj)-1
        #Inicializamos los centroides aleatoriamente
        m = [conj[randint(0,N)] for _ in range(k)] 
        m_ant = None
        while m != m_ant:
            m_ant = m.copy()
            min_dist = 100
            cent = None
            clusters = [[] for _ in range(k)]
            for j in range(N):
                for i in range(k):
                    dist = kmedias.euclidea(conj[j],m[i])
                    if dist < min_dist:
                        min_dist = dist
                        cent = i
                clusters[cent].append(conj[j])
                
            print(clusters)
                
        print(m)       
        
    def euclidea(x,y):
        for j in range(len(x)):
            dis += (x[j]-y[j])**2
        return sqrt(dis)
        
        

conj = [51, 43, 62, 64, 45, 42, 46, 45, 45, 62, 47, 52, 64, 51, 65, 48, 49, 46, 64, 51, 52, 62, 49, 48,
        62, 43, 40, 48, 64, 51, 63, 43, 65, 66, 65, 46, 39, 62, 64, 52, 63, 64, 48, 64, 48, 51, 48, 64, 42, 48, 41]      
kmedias(2,conj,3)
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 11:54:07 2017

@author: JM
"""
import math

def media(x):
	media = 0	
	for score in x.values():
		media += score
	return (media / len (x.values()))

"""
Recibe los items, usuarios que han puntuado los dos items y el conjunto de todos los usuarios
"""
def similarity(item1, item2, users, conj):
    num = 0
    den1 = 0
    den2 = 0
    for user in users:
        median = media(conj[user])
        score1 = conj[user].get(item1)
        score2 = conj[user].get(item2)
        num += (score1 - median) * (score2 - median)
        den1 += (score1 - median)**2
        den2 += (score2 - median)**2
    den1 = math.sqrt(den1)
    den2 = math.sqrt(den2)
    return (num/(den1*den2))

"""
A partir de un item, el conjunto de todos los usuarios y el conjunto de todos los items,
calcula los items mas similares y que superen el umbral 
"""
def neighborhood(x,conj_user,conj_item,threshold):
    neighborhood = {}
    sim = 0
    itemX = conj_item.get(x)
    #Recorremos todos los items
    for item in conj_item:
        users = []
        if item != x:
            itemY = conj_item.get(item)
            #Para cada item obtenemos todos los usuarios puntuados
            for user in itemY:
                #Comprobamos si el usuario existe puntuado en la lista del item recibido
                if user in itemX:
                    users.append(user)
            print("Usuarios que han puntuado",x,item, users)
            sim = similarity(x,item,users,conj_user)
            print("Similaridad:",sim)
            #Si la similaridad supera el umbral, lo consideramos vecino
            if(sim >= threshold):
                neighborhood[item] = sim
    return neighborhood

"""
a = Usuario
p = Item no puntuado
conj_user = Conjunto de los usuarios con sus items puntuados
conj_item = Conjunto de los items con los usuarios que lo han puntuado
threshold = Umbral de vecindad
"""
def prediction (a, p, conj_user,conj_item, threshold):
    neighbors = neighborhood(p, conj_user,conj_item, threshold)
    num = 0
    den = 0
    #Recorremos todos los items similares al item que queremos calcular
    for item in neighbors:
        #Elegimos solo los items similares que han sido votados por el usuario "a"
        if item in conj_user[a]: 
            score = conj_user[a][item]
            sim = neighbors.get(item)
            num += (sim*score)
            den += sim
            print("Sim",sim,"Score",score) 
    return (num/den)
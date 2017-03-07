# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 14:18:25 2017

@author: JM
"""
import userRecommendation as userR
import itemRecommendation as itemR

# diccionario de diccionario para almacernar los datos en funcion de los usuarios
# {userId : {peliculaID : valoracion, ...},...}
def userDict(pathToFile):
	user = dict()
	#user id | item id | rating | timestamp
	with open (pathToFile) as raw_data:
		for item in raw_data:
						
			userID,filmID,rating,_=item.split("\t")
			if(userID not in  user):			
				user[userID]={filmID:rating}
							
			else:
				user.get(userID)[filmID]=rating
	return user
 
# diccionario de diccionario para almacernar los datos en funcion de los items
# {userId : {peliculaID : valoracion, ...},...}
def itemDict(pathToFile):
	dictionary = dict()
	#user id | item id | rating | timestamp
	with open (pathToFile) as raw_data:
		for item in raw_data:					
			userID,filmID,rating,_=item.split("\t")
			if(filmID not in  dictionary):			
				dictionary[filmID]={userID:rating}
							
			else:
				dictionary.get(filmID)[userID]=rating
	return dictionary

"""
Define el ejemplo de la pagina 6
Modificado para que sea usando diccionarios
{userId : {peliculaID : valoracion, ...},...}
{peliculaId : {userID : valoracion, ...},...}
"""
def example():
    conj_user = {"a":{1:5,2:3,3:4,4:4},
            "b":{1:3,2:1,3:2,4:3,5:3},
            "c":{1:4,2:3,3:4,4:3,5:5},
            "d":{1:3,2:3,3:1,4:5,5:4},
            "e":{1:1,2:5,3:5,4:2,5:1},
           }
    conj_item = {1:{"a":5,"b":3,"c":4,"d":3,"e":1},
            2:{"a":3,"b":1,"c":3,"d":3,"e":5},
            3:{"a":4,"b":2,"c":4,"d":1,"e":5},
            4:{"a":4,"b":3,"c":3,"d":5,"e":2},
            5:{"b":3,"c":5,"d":4,"e":1},
           }
    return conj_user,conj_item

#------------------------- Prueba con ejemplo de teoría ---------------------
conj1,conj2 = example()

print("----- Ejemplo teoria con recomendacion en usuarios ------")
print("Usuarios vecinos de A", userR.neighborhood("a",conj1,0.6))
print("Prediccion de la puntuacion del item 5 para el usuario A:",userR.prediction("a",5,conj1,0.6))

print("----- Ejemplo teoria con recomendacion en items ------")
print("Items vecinos de 1", itemR.neighborhood(1,conj1,conj2,0.6))
print("Prediccion de la puntuacion del item 5 para el usuario A:",itemR.prediction("a", 5, conj1,conj2, 0.6))

#------------- Prueba con el conjunto de datos de peliculas -----------------  
userDict("u.data") 
itemDict("u.data")

from scipy.stats.stats import pearsonr

# diccionario de diccionario para almacernar los datos
# {userId : {peliculaID : valoracion, ...},...}
def diccionarioUsuario(pathToFile):
	user = dict()
	
	with open (pathToFile) as raw_data:
		for item in raw_data:
						
			userID,filmID,rating,_=item.split("\t")
			if(userID not in  user):			
				user[userID]={filmID:rating}
							
			else:
				user.get(userID)[filmID]=rating

	print (user)

"""
Define el ejemplo de la pagina 6
Modificado para que sea usando diccionarios
"""
def userExample():
    conj = {"a":{1:5,2:3,3:4,4:4},
            "b":{1:3,2:1,3:2,4:3,5:3},
            "c":{1:4,2:3,3:4,4:3,5:5},
            "d":{1:3,2:3,3:1,4:5,5:4},
            "e":{1:1,2:5,3:5,4:2,5:1},
           }
    return conj

# x: dataset
# y: dataset
def similarity(x,y):
	r,_= pearsonr(x, y)
	return (r)


# x: dataset
def media(x):
	media = 0	
	for score in x.values():
		media += score
	return (media / len (x.values()))

"""
A partir del conjunto de usuarios y del usuario a comprobar la similaridad,
 devuelve el conjunto de vecinos que supera el umbral de similaridad dado.
"""
def neighborhood(x,conj,threshold):
    neighborhood = {}
    sim = 0
    itemX = conj.get(x)
    #Recorremos todos los usuarios
    for user in conj:
        valx = []
        valy = []
        if user != x:
            itemY = conj.get(user)
            #Para cada usuario obtenemos todos los items puntuados
            for item in itemY:
                #Comprobamos si el item existe puntuado en la lista del usuario recibido
                if item in itemX:
                    print("Existe item", item)
                    valx.append(itemX.get(item))
                    valy.append(itemY.get(item))
            print("Val x", valx)
            print("Val y", valy)
            sim = similarity(valx,valy)
            print("Similaridad:",sim)
            #Si la similaridad supera el umbral, lo consideramos vecino
            if(sim >= threshold):
                neighborhood[user] = sim
    return neighborhood

# a : dataset
# p : object not in a
# N : set of dataset
def prediction (a, p, N, threshold):
    pred = 0
    neighbors = neighborhood(a,N, threshold)
    ra = media(N.get(a))
    pred += ra
    num = 0
    den = 0
    for user in neighbors:
        rb = media(N.get(user))
        sim = neighbors.get(user)
        score = N.get(user).get(p)
        num += (sim*(score-rb))
        den += sim
        print("Media",rb,"Sim",sim,"Score",score)
    pred += num/den
    return pred

#diccionarioUsuario("u.data")
conj = userExample()
#print(conj)


#print (neighborhood("a",conj,0.6))
print(prediction("a",5,conj,0.6))

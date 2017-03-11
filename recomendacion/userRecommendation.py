from scipy.stats.stats import pearsonr
import math

# x: dataset
# y: dataset
def similarity(x,y):
    num = 0
    den1 = 0
    den2 = 0
    for i in range(len(x)):
        ra = mediaList(x)
        rb = mediaList(y)
        #print("Valor media X", ra, "Valor media Y", rb)
        num += (x[i]-ra)*(y[i]-rb)
        den1 += (x[i]-ra)**2
        den2 += (y[i]-rb)**2
       # print("numerador", num, "den1", den1,"den2", den2)
    den1 = math.sqrt(den1)
    den2 = math.sqrt(den2)
    if num != 0 and den1 != 0 and den2 != 0:
        return (num/(den1*den2))
    else:
        return 0

# x: dataset
def media(x):
	media = 0	
	for score in x.values():
		media += score
	return (media / len (x.values()))

def mediaList(x):
   media = 0	
   for score in x:
       media += score
   return (media / len (x)) 

"""
A partir del conjunto de usuarios y del usuario a comprobar la similaridad,
 devuelve el conjunto de vecinos que supera el umbral de similaridad dado.
"""
def neighborhood(x,conj,threshold):
    neighborhood = {}
    itemX = conj.get(x)
    #print("ItemX",itemX,"X",x)
    #Recorremos todos los usuarios
    for user in conj:
        sim = 0
        valx = []
        valy = []
        if user != x:
            itemY = conj.get(user)
            #Para cada usuario obtenemos todos los items puntuados
            for item in itemY:
                #Comprobamos si el item existe puntuado en la lista del usuario recibido
                if item in itemX:
                    #print("Existe item", item)
                    valx.append(itemX.get(item))
                    valy.append(itemY.get(item))
            #print("Val x", valx)
            #print("Val y", valy)
            if len(valx) > 1:
                sim = similarity(valx,valy)
            #print("Similaridad:",sim)
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
        if p in N.get(user):
            rb = media(N.get(user))
            sim = neighbors.get(user)
            score = N.get(user).get(p)
            num += (sim*(score-rb))
            den += sim 
            #print("Media",rb,"Sim",sim,"Score",score)
    pred += num/den
    return pred
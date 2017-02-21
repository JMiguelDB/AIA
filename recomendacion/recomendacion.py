
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

#Define el ejemplo de la pagina 6
def example():
    a = [5,3,4,4]
    b = [3,1,2,3,3]
    c = [4,3,4,3,5]
    d = [3,3,1,5,4]
    e = [1,5,5,2,1]
    conj = [a,b,c,d,e]
    return conj

# x: dataset
# y: dataset
def similarity(x,y):
	r,_= pearsonr(x, y)
	return (r)


# x: dataset
def media(x):
	media = 0	
	for i in range(len(x)):
		media +=x[i]
	return (media / len (x))

# x: dataset
# y: dataset
def equalItems(x,y):
    lenx = len(x)
    leny = len(y)
    elements = abs(lenx - leny)
    if(lenx > leny):
        for i in range(elements):
            x.pop()
    elif(leny > lenx):
        for i in range(elements):
            y.pop()
    return x,y

#A partir del conjunto de usuarios y del usuario a comprobar la similaridad,
# devuelve el conjunto de vecinos que supera el umbral de similaridad dado.
def neighborhood(x,conj,threshold):
    neighborhood = []
    sim = 0
    valx = x[:]
    valy = []
    for i in range(len(conj)):
        valy = conj[i][:]
        valx, valy = equalItems(valx,valy)
        sim = similarity(valx,valy)
        print("Similaridad:",sim)
        if(sim >= threshold and valx != valy):
            neighborhood.append(conj[i])
    print(conj)
    return neighborhood
# a : dataset
# p : object not in a
# N : set of dataset
def prediction (a ,p ,N):
	r = media(a)
	for i in range (len(N)):
		aux = v.remove(p)	
		print (similarity(a,aux))


#diccionarioUsuario("u.data")
conj = example()
print(conj)


print (neighborhood(conj[0],conj,0.6))

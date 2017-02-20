
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
a = [5,3,4,4]
b = [3,1,2,3,3]
c = [4,3,4,3,5]
d = [3,3,1,5]
e = [1,5,5,2]

ve = [b,c]


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

# a : dataset
# p : object not in a
# v : set of dataset
def prediction (a ,p ,v):
	r = media(a)
	for i in range (len (v)):
		aux = v.remove(p)	
		print (similarity(a,aux))


diccionarioUsuario("u.data")
print (prediction(a,3,ve))

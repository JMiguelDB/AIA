import nltk
import sklearn
import math
from sklearn.feature_extraction.text import CountVectorizer #implemetacion del tokenizar y contador de ocurrencias
#nltk.corpus.stopwords.words("spanish")
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
corpus = [
	    "éste texto no tiene nada que ver con los demás",
	    "la plata fue entregada en camiones color plata",
	    "el cargamento de oro llegó en un camión. El cargamento de oro llegó en un camión. El cargamento de oro llegó en un camión",
	    "cargamentos de oro dañados por el fuego",
	    "el cargamento de oro llegó en un camión",
	]
texto = "oro plata camion"



def inicializaVectorizador(corpus):

	
	vectorizador = CountVectorizer(min_df=1)#inicialización del vectorizador
	datos = vectorizador.fit_transform(corpus) #vectoriza el corpus
		
	vector = datos.toarray()
	
	return vectorizador ,vector
	#analiza = vectorizador.transform(['oro plata camión']).toarray() #vectoriza el texto que queremos probar
	#print(test)

def vectorizaPrueba(vectorizador,texto):
	prueba = vectorizador.transform([texto]).toarray()	
	return prueba


def calculaDistanciaEuclidea(vectorInicial, vectorAnalizar):
	distancias = []
	for i in range (len (vectorInicial)):
		distancias.append((distanciaEuclidea(vectorInicial[i],vectorAnalizar[0]),i))		
	return sorted(distancias)

def distanciaEuclidea(valor1, valor2):
	acu = 0
	for i in range(len(valor1)):
		#print (valor1[i])		
		acu = acu + (valor1[i] - valor2[i])**2
	
	return math.sqrt(acu)


def distanciaNormalizada(vectorInicial, vectorAnalizar):
	lista =[]
	for i in range(len(vectorInicial)):
		sumaVA = 0 #sumatorio del vector que hay que analizar
		sumaVI = 0 #sumatorio del vector inicial
		sumaTotal = 0	
		for j in range(len(vectorInicial[i])):
			sumaVI= sumaVI + vectorInicial[i][j]**2
			sumaVA = sumaVA + vectorAnalizar[0][j]**2 		
			sumaTotal = sumaTotal + vectorInicial[i][j]+vectorAnalizar[0][j]
		valor = sumaTotal /(math.sqrt(sumaVI)*math.sqrt(sumaVA))
		lista.append((valor,i))		
	return sorted(lista)	


def filtra(corpus,stop):
	corpusFil= []	
	for frase in corpus:
		
		palabras = frase.split()		
		frase = ""	
		for palabra in palabras:	
			if palabra not in stop:			
				frase =frase+ (palabra)
				frase = frase + " "
		corpusFil.append(frase) 	
	return corpusFil

def raiz(corpus,stemmer):
	corpusStem=[]
	for frase in corpus:
		palabras = frase.split()
		frase = ""
		for palabra in palabras:
			frase = frase + stemmer.stem(palabra)
			frase = frase + " "
		corpusStem.append(frase)
	return corpusStem



#inicialización de las características
vectorizador,vectorInicial=inicializaVectorizador(corpus)
vectorAnalizar = vectorizaPrueba(vectorizador,texto)

print("--------------------Paso 1 ----------------------------------")
euclideas = calculaDistanciaEuclidea(vectorInicial, vectorAnalizar)
print ("distancias euclideas ordenadas:",  euclideas)

print("--------------------Paso 2 ----------------------------------")
normales = distanciaNormalizada(vectorInicial,vectorAnalizar)
print ("distancias normales ordenadas:",normales)




print("--------------------Paso 3 ----------------------------------")

	#filttrado de stopwords
stop = set(stopwords.words("spanish"))
corpusFil = filtra(corpus, stop)
	#inicializacion de caracteristicas

vectorizadorFil,vectorInicialFil = inicializaVectorizador(corpusFil)
vectorAnalizarFil = vectorizaPrueba(vectorizadorFil,texto)
	#distancia euclidea

euclideasFil = calculaDistanciaEuclidea(vectorInicialFil, vectorAnalizarFil)
print ("distancias euclideas sin stop words ordenadas:", euclideasFil)

normalFil=distanciaNormalizada(vectorInicialFil,vectorAnalizarFil)
print ("distancias normalizadas sin stop words ordenadas:", normalFil)

#print (normales)

print("--------------------Paso 4 ----------------------------------")

#inicializa variables
stemmer = SnowballStemmer("spanish")
corpusStem = raiz(corpusFil,stemmer)
textoStem = "oro plat camion"

vectorizadorStem,vectorInicialStem = inicializaVectorizador(corpusStem)
vectorAnalizarStem = vectorizaPrueba(vectorizadorStem,textoStem)

euclideasStem = calculaDistanciaEuclidea(vectorInicialStem, vectorAnalizarStem)
print ("distancias euclideas sin stop words y stemmatizadas ordenadas:", euclideasStem)
normalStem=distanciaNormalizada(vectorInicialStem,vectorAnalizarStem)
print ("distancias normalizadas sin stop words y stemmatizadas ordenadas:", normalStem)

#print (stop)

print ("----------------------paso 5 -----------------------------")

def tfid(corpus, texto, stopWords):
	#vect = ect = TfidfVectorizer(sublinear_tf=True, max_df=0.5, analyzer=texto,stop_words='spanish', vocabulary=corpus[0])
	#vect.fit(corpus)	
	
	vectorizador = TfidfVectorizer(min_df=1)
	datos = vectorizador.fit_transform(corpus)	
	vector = datos.toarray()	
	return vectorizador ,vector


vectorizadorTF, vectorInicialTF= tfid(corpusStem,textoStem,stop)
euclideasTF = calculaDistanciaEuclidea(vectorInicialTF, vectorAnalizarStem)
print ("distancias euclideas TF:", euclideasStem)
normalTF=distanciaNormalizada(vectorInicialTF,vectorAnalizarStem)
print ("distancias normalizadas TF:", normalStem)






from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
import re
from sklearn.cluster import KMeans
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer



from sklearn import metrics


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

def inicializaVectorizador(corpus):

	
	vectorizador = CountVectorizer(min_df=1)#inicialización del vectorizador
	datos = vectorizador.fit_transform(corpus) #vectoriza el corpus
		
	vector = datos.toarray()
	
	return vectorizador ,vector


def inicializaVectorizador(corpus):
	vectorizador = CountVectorizer(min_df=1)#inicialización del vectorizador
	datos = vectorizador.fit_transform(corpus) #vectoriza el corpus	
	vector = datos.toarray()	
	return vectorizador ,vector

def vectorizaPrueba(vectorizador,texto):
	prueba = vectorizador.transform(texto).toarray()	
	return prueba



def inicializa():
	# carga del corpus
	clase = []	
	categories =["comp.graphics","comp.os.ms-windows.misc","comp.sys.ibm.pc.hardware","comp.sys.mac.hardware","comp.windows.x","sci.space"]
	stemmer = SnowballStemmer("english")
	stop = set(stopwords.words("english"))
	corpus = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)	
	#print(type(corpus),corpus)	
	corpusData = corpus.data	
	corpusFil = filtra(corpusData,stop)
	corpusSte = raiz(corpusFil,stemmer)
	for t in corpus.target[:len(corpus.target)]:	
		clase.append((corpus.target_names[t]))		
	return corpusSte,clase
	
def devuelveMasRelacionado(distancias, clase):
	valor =[]
	for a,b in zip(distancias, clase):
		valor.append((a, b))
	valor= sorted(valor)	
	return valor[0]

def tfid(corpus):
	vectorizador = TfidfVectorizer(min_df=1)
	datos = vectorizador.fit_transform(corpus)	
	vector = datos.toarray()	
	return vectorizador ,vector

texto = ["space NASA moon stars"]

corpusTratado,clase = (inicializa())
#print(len(clase),len(corpusTratado))
print("--------------------------distancia euclidiana--------------------------")

vectorizadorFil,vectorInicialFil = tfid(corpusTratado)

#vectorizadorFil,vectorInicialFil = inicializaVectorizador(corpusTratado)
vectorAnalizarFil = vectorizaPrueba(vectorizadorFil,texto)
#print ("vi:", len (vectorInicialFil), "VA::",vectorAnalizarFil)
distancias = (euclidean_distances(vectorInicialFil, vectorAnalizarFil))
valor = devuelveMasRelacionado(distancias,clase)
print(valor)
print("---------------------------distancia normal-----------------------------")

distanciasCoseno = cosine_similarity(vectorInicialFil, vectorAnalizarFil)
valorCoseno = devuelveMasRelacionado(distanciasCoseno,clase)
print(valorCoseno)

print("----------------------------Kmeans--------------------------------------")

kmeans = KMeans(n_clusters=6, max_iter=40, n_init=2).fit(vectorInicialFil)
labelTexto = kmeans.predict(vectorAnalizarFil) # cluster al que pertenece la prueba
#print(kmeans.labels_) #cluster para cada elemento

# unir los datos y la etiqueta
def uneDatos(corpus, kmeans):
	datos = []	
	for a,b in zip (corpus, kmeans):
		datos.append((a,b))
	
	return datos

datos = uneDatos(corpusTratado, kmeans.labels_)

#filtrado 

def filtra(datos,labelTexto ):
	filtrados = []	
	for i in range (len(datos)):
		
		if(int (datos[i][1])== int (labelTexto)):			
			filtrados.append(datos[i][0])
	
	return (filtrados)

datosFiltrados = filtra(datos,labelTexto)




vectorizadorK,vectorInicialK = tfid(datosFiltrados)
textoK = vectorizaPrueba(vectorizadorK,texto)
distanciasCoseno = cosine_similarity(vectorInicialFil, vectorAnalizarFil)
datosOrdenados = uneDatos(datosFiltrados,distanciasCoseno)
datosOrdenados = sorted(datosOrdenados)
print(labelTexto)
print(datosOrdenados[0])

def rendimiento(datosOrdenados,texto):
	resultados=[]
	for i in range(len(datosOrdenados)):
		letras = datosOrdenados[i][0].split()		
		palabras = 0	
		for i in range(len(letras)):
			#print(letras[i], texto[0])			
			if(letras[i] in texto[0]):
							
				palabras = palabras +1		
		resultados.append(palabras/len(letras))
	return resultados
print(rendimiento(datosOrdenados,texto))







import numpy
import random
#epsilon: posibilidad de equivocarse
#1-epsilon: posibilidad de no equivocares
##
##          [x][ ][ ]
##          [ ][o][x]	
##          [ ][x][ ] 
##    probabilidad de acertar e(1-3)³
##probabilidad de transición 1/casillas libres


## las posibles movientos están codificados, N S E O




class cuadricula():
#m: nº de filas
#n: nº de filas
	
	
	
	
	def __init__(self,m,n):		
		self.pi= []
		self.transiciones=[[]]
		self.observaciones=["N","S","E","O","EO","SO","SE","SEO","NO","NE","NEO","NS","NSO","NSE","NSEO",""]
		self.estados=[]
		self.m = m
		self.n = n
		self.acu = 0		
		s = (m,n)
		self.tablero = numpy.ones(s)
		for i in range(m):
			for j in range(n):
				if (random.randint(1,2)==1):				
					#self.acu += 1
									
					self.tablero[i][j]=0
					#self.estados.append((i,j))
	
	def getEstados(self):
		return self.estados

	def getTablero():
		return self.tablero

	def iniciaPi(self):
		aux = 1/len(self.estados)
			
		for i in range(len(self.estados)):
			self.pi.append(aux)	
		return self.pi		
	
	def getTransiciones(self):
		lista =[]		
		horizontal = len(self.tablero)-1
		vertical = len(self.tablero)-1		
		for i in range(len(self.tablero)):		
			for j in range(len(self.tablero[i])):		
				a=[]			
				if (self.tablero[i][j] !=0 ):
															
					if ((i-1 >= 0) and (j <= vertical) and (i <= horizontal) and self.tablero[i-1][j]== 1 ):
						a.append([i-1 ,j]) #N
					if ((i>= 0) and (j <= vertical) and (i < horizontal) and  self.tablero[i+1][j]== 1 ):
						a.append([i+1 ,j]) #S
					if ((j > 0) and (j <= vertical) and (i <= horizontal) and self.tablero[i][j-1]== 1 ):
						a.append([i ,j-1]) #O					
					if ((j >= 0) and (j < vertical) and (i <= horizontal) and self.tablero[i][j+1]== 1 ):
						a.append([i ,j+1]) #E
					lista.append(a)

		listaDeEstados = []		
		for i in range (len(self.estados)):
			estadoIn = []
			if (len(lista[i])!=0):			
				probabilidades= 1/len(lista[i])
				print (probabilidades)		
			for j in range(len(self.estados)):
				for z in range(len(lista[i])):				
					print (self.estados[j],lista[i][z])					
					if (self.estados[j] in lista[i][z]):
						print ("true")							
						estadoIn.append(probabilidades)
					else:
						estadoIn.append(0)

			listaDeEstados.append(estadoIn)
		print ("lista ",listaDeEstados)
		




		print (len(lista))		
		return lista			
	

#	def getTrans():
		
	def listaEstados(self):
		#estados = numpy.zeros(len (self.tablero),len(self.tablero[0]))
		for i in range(len(self.tablero)):		
			for j in range(len(self.tablero[i])):						
				if (self.tablero[i][j] == 1):				
					self.estados.append([i,j])
					#print(i,j)				
				#print(listaEstados)
		return self.estados

	



a = cuadricula(5,5)


print (a.tablero)

pi=[]

#print(a.getEstados())
print("estados", (a.listaEstados()))
pi= a.iniciaPi()
print(len(pi))

print (a.getTransiciones())








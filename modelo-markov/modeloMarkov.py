
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
					self.acu = self.acu + 1					
					self.tablero[i][j]=0
					self.estados.append((i,j))
	
	def getEstados(self):
		return self.estados

	def getTablero():
		return self.tablero

	def iniciaPi(self):
		aux = 1/self.acu		
		for i in range(self.acu):
			self.pi.append(aux)	
		return self.pi		
	
	def getTransiciones(self):
		lista =[]		
		for i in range(len(self.tablero)):		
			for j in range(len(self.tablero[i])):		
				a  =""				
				if (self.tablero[i][j] !=0 ):									
					if ((i-1 >= 0) and (j<= 3) and (i <= 3) and self.tablero[i-1][j]== 1 ):
						a +=str(i-1) + "," + str(j)+" " #N
					if ((i >= 0) and (j<= 3)and (i < 3) and  self.tablero[i+1][j]== 1 ):
						a +=str(i+1) + "," + str(j)+" " #S
					if ((j > 0) and (j <= 3)and (i <= 3) and self.tablero[i][j-1]== 1 ):
						a +=str(i) + "," + str(j-1)+" " #O
					if ((j >= 0) and (j<3)and (i <= 3) and self.tablero[i][j+1]== 1 ):
						a +=str(i) + "," + str(j+1)+" "	#E	
					else:
						a = a + ("")
				lista.append(a)
		return lista			
	

#	def getTrans():
		



a = cuadricula(4,4)


print (a.tablero)
(a.acu)
pi=[]
pi= a.iniciaPi()
#print(a.getEstados())
#print(pi)
print (a.getTransiciones())









import numpy
import random
# epsilon: posibilidad de equivocarse
# 1-epsilon: posibilidad de no equivocarse
##
##          [x][ ][ ]
##          [ ][o][x]    
##          [ ][x][ ] 
##    probabilidad de acertar e(1-3)³
##probabilidad de transición 1/casillas libres


## las posibles movientos están codificados, N S E O

class cuadricula():
    #m: nº de filas
    #n: nº de columnas
    #error: Probabilidad de error al realizar las observaciones
    def __init__(self,m,n, epsilon):   
        self.tablero = self.generaTablero(m,n)
        """
        self.tablero = [
           [0,1,1],
           [1,1,1],
           [1,0,1]
           ]  
        """
        self.estados= self.listaEstados()
        self.observaciones=["N","S","E","O","EO","SO","SE","SEO","NO","NE","NEO","NS","NSO","NSE","NSEO",""]
        self.pi= self.iniciaPi()
        self.transiciones = self.matrizA()
        self.sensor = self.matrizB(epsilon)
        
        
        
    def generaTablero(self,m,n):
        s = (m,n)
        tablero = numpy.ones(s)
        for i in range(m):
            for j in range(n):
                if (random.randint(1,2)==1):                
                    tablero[i][j]=0
        return tablero
    
    def listaEstados(self):
        estados = []
        for i in range(len(self.tablero)):        
            for j in range(len(self.tablero[i])):                        
                if (self.tablero[i][j] == 1):                
                    estados.append([i,j])
        return estados
 

    def iniciaPi(self):
        aux = 1/len(self.estados)
        pi = []
        for i in range(len(self.estados)):
            pi.append(aux)    
        return pi        
    
    def matrizA(self):
        lista = []        
        horizontal = len(self.tablero)-1
        vertical = len(self.tablero)-1 
        #Se generan los vecinos de cada estado
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
        
        #Lista en el que a cada estado se le asocia la probabilidad de ir al resto de estados
        listaDeProbabilidades = []        
        for i in range (len(self.estados)): 
            estadoIn = []
            probabilidades = 0
            if (len(lista[i])!=0):            
                probabilidades = 1/len(lista[i])       
            for j in range(len(self.estados)):              
                if (self.estados[j] in lista[i]):                           
                    estadoIn.append(probabilidades)
                else:
                    estadoIn.append(0)
            listaDeProbabilidades.append(estadoIn)
        #print ("lista ",lista)  
        #print ("probabilidades ",listaDeProbabilidades)  
        return listaDeProbabilidades 

    def matrizB(self, epsilon):   
        lista = []        
        horizontal = len(self.tablero)-1
        vertical = len(self.tablero)-1 
        #Se generan los vecinos de cada estado
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
        #Se genera una lista del valores de las observaciones para cada estado           
        listaDeObservaciones = []
        for i in range (len(self.estados)): 
            estadoIn = []      
            for j in range(len(self.observaciones)):              
                observacion = self.observaciones[j]
                error = 1
                estado = [] 
                #Se recorren los distintos vecinos y se comprueba si la observacion es equivocada o no
                for direccion in 'NSOE':
                    if direccion == 'N':
                        estado = [self.estados[i][0]-1,self.estados[i][1]]
                    elif direccion == 'S':
                        estado = [self.estados[i][0]+1,self.estados[i][1]]
                    elif direccion == 'O':
                        estado = [self.estados[i][0],self.estados[i][1]-1]
                    elif direccion == 'E':
                        estado = [self.estados[i][0],self.estados[i][1]+1]
                    
                    if estado in lista[i]:
                        if direccion in observacion:
                            error = error * epsilon
                        else:
                            error = error * (1 - epsilon)
                    else:
                        if direccion in observacion:
                            error = error * (1 - epsilon) 
                        else:
                            error = error * epsilon
                estadoIn.append(error)
            listaDeObservaciones.append(estadoIn)
        return listaDeObservaciones
                        
    def evaluaAvance(self,estado,estadoCalculado):
        return abs(estado[0] - estadoCalculado[0]) + abs(estado[1] - estadoCalculado[1])
    

"""

a = cuadricula(5,5, 1/10)

print (a.tablero)
print("estados", a.estados)
print("observaciones", a.observaciones)
print("pi", a.pi)
print("Matriz A", a.transiciones)
print("Matriz B", a.sensor)
print("Prueba error avance", a.evaluaAvance([1,0],[4,3]))
#print(a.getEstados())

#print(len(pi))

#print (a.getTransiciones())

"""






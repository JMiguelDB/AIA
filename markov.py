# -*- coding: utf-8 -*-

#Aqui se almacenan las probabilidades
#Recibe matriz A: Matriz de n x n de transición de todos los n posibles casos (matriz dispersa). 
#Recibe matriz B: Matriz de observaciones almacena todos los posibles cambios de estado(flechas del grafo)
#Recibe el vector pi: Vector de tamaño de los posibles estados que almacena la probabilidad del estado inicial
#Recibe la lista de los posibles estados
#Recibe la lista de las posibles observaciones
#Crear los algoritmos Viterbi, avance y muestreo
class modOculMarkov:
    def __init__(self, A, B, pi, estados, observaciones):
        self.transiciones = A
        self.sensor = B
        self.probEstInicial = pi
        self.estados = estados
        self.observacion = observaciones
    
    
    #Devuelve los valores alfa de cada n estado para el ultimo instante(ultima observacion)
    def avance(modOculMarkov, posiblesObservaciones):
        alpha=[]
        indice = modOculMarkov.observacion.index(posiblesObservaciones[0])
        rangoEstados = range(len(modOculMarkov.estados)) #Rango con todos los posibles estados
        #Generacion de la probabilidad del primer instante(paso 1)
        for i in rangoEstados:
            alpha.append(modOculMarkov.sensor[i][indice] * modOculMarkov.probEstInicial[i])
            
        rangoPosObs = range(1,len(posiblesObservaciones)) #Rango de las posibles observaciones tomadas
        #Generacion de la probabilidad de los siguientes instantes
        for obs in rangoPosObs:
            indice = modOculMarkov.observacion.index(posiblesObservaciones[obs])
            for i in rangoEstados:
                for estados in modOculMarkov.transiciones[i]:
                    
                #Terminar
                #alpha[i] = modOculMarkov.sensor[i][indice] * modOculMarkov.probEstInicial[i]
                res = 0
        #return alpha
        print(alpha)
        
        
    def viterbi():
        return result
        
    def muestreo():
        return result
#Ejemplo pag. 28
# Lista: [Lluvia[lluvia, no-lluvia],No-lluvia[lluvia, no-lluvia]]        
A = [[0.7,0.3],[0.7,0.3]]
# Lista: [Lluvia[paraguas, no-paraguas], no-lluvia[paraguas, no-paraguas]]
B = [[0.9,0.1],[0.2,0.8]]
pi = [0.5,0.5]
estados = ['lluvia','no-lluvia']
observaciones = ['paraguas','no-paraguas']
prueba = modOculMarkov(A,B,pi,estados,observaciones)
posiblesObservaciones = ['paraguas','paraguas','no-paraguas']
#print(prueba.estados)
#print(modOculMarkov.avance(prueba,posiblesObservaciones))
modOculMarkov.avance(prueba,posiblesObservaciones)

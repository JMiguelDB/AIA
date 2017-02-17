# -*- coding: utf-8 -*-
import random
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
        print(alpha)     
        #Generacion de la probabilidad de los siguientes instantes
        rangoPosObs = range(1,len(posiblesObservaciones)) #Rango de las posibles observaciones tomadas
        for obs in rangoPosObs:
            indice = modOculMarkov.observacion.index(posiblesObservaciones[obs])
            antAlpha = alpha[:]
            print("Observacion: ", obs)
            for i in rangoEstados:
                valor = 0
                print("Estado: ", i)
                for estado in rangoEstados:
                    valor += modOculMarkov.transiciones[i][estado] * antAlpha[estado]
                    print(modOculMarkov.transiciones[i][estado],'*' , antAlpha[estado])
                alpha[i] = modOculMarkov.sensor[i][indice] * valor
                print("Valor nuevo alpha: ", alpha)
        return alpha
        
    #Devuelve la secuencia de estados mas probables para las observaciones tomadas   
    def viterbi(modOculMarkov, posiblesObservaciones):
        viterbi=[]
        prob={} #Diccionario con: "instante - Estado" = probabilidad de ese estado en ese instante
        indice = modOculMarkov.observacion.index(posiblesObservaciones[0])
        rangoEstados = range(len(modOculMarkov.estados)) #Rango con todos los posibles estados
        #Generacion de la probabilidad del primer instante(paso 1)
        for i in rangoEstados:
            viterbi.append(modOculMarkov.sensor[i][indice] * modOculMarkov.probEstInicial[i])
            prob['0-'+str(i)] = ''
        print(viterbi)
        print(prob)
        rangoPosObs = range(1,len(posiblesObservaciones)) #Rango de las posibles observaciones tomadas
        #Generamos los valores de viterbi y las probabilidades de cada estado
        for obs in rangoPosObs:
            indice = modOculMarkov.observacion.index(posiblesObservaciones[obs])
            antViterbi = viterbi[:]
            print("Observacion: ", obs)
            for i in rangoEstados:
                valor = 0
                print("Estado: ", i)
                for estado in rangoEstados:
                    valorActual = modOculMarkov.transiciones[i][estado] * antViterbi[estado]
                    if valor < valorActual:
                        valor = valorActual
                        prob[str(obs)+'-'+str(i)] = estado
                    print(modOculMarkov.transiciones[i][estado],'*' , antViterbi[estado])
                viterbi[i] = modOculMarkov.sensor[i][indice] * valor
                print("Valor nuevo viterbi: ", viterbi)
                print("Valor estados: ", prob)
            #Calculamos la probabilidad de la ultima observacion y extraemos los estados mas probables para llegar a ese estado
            if obs == len(posiblesObservaciones)-1:
                valor = 0
                estados=[]
                for estado in rangoEstados: 
                    if valor < viterbi[estado]:
                        valor = viterbi[estado]
                        ultimoEstado = estado
                estados.append(modOculMarkov.estados[ultimoEstado])
                for n in range(len(posiblesObservaciones)-1,0,-1):
                    ultimoEstado = prob[str(n)+'-'+str(ultimoEstado)]
                    estados.append(modOculMarkov.estados[ultimoEstado])
                print(list(reversed(estados)))
        return list(reversed(estados))
    
    #Asigna una observacion para un estado dado a partir un numero aleatorio
    def generaObservaciones(self,estado):
       numeroAleatorio = random.random()
       print("Numero aleatorio observacion:",numeroAleatorio)
       prob = 0
       valor = ""
       for observacion in range(len(self.sensor[estado])):
           prob += self.sensor[estado][observacion]
           if numeroAleatorio < prob:
               valor = self.observacion[observacion]
               break
       return valor
               
        
    #Genera una secuencia de "n" estados y observaciones de esos estados   
    def muestreo(modOculMarkov, numEstados):
        secEstados = []
        secObservaciones = []
        estadoActual = 0
        for estado in range(numEstados):
            numeroAleatorio = random.random()
            print("Numero aleatorio estado:",numeroAleatorio)
            if estado == 0:
                valor = 0
                for i in range(len(modOculMarkov.probEstInicial)):
                    valor += modOculMarkov.probEstInicial[i]
                    if numeroAleatorio < valor:
                        secEstados.append(modOculMarkov.estados[i])
                        secObservaciones.append(modOculMarkov.generaObservaciones(i))
                        estadoActual = i
                        break
                print(secEstados,secObservaciones)
            else:
               valor = 0
               for i in range(len(modOculMarkov.transiciones[estadoActual])):
                   valor += modOculMarkov.sensor[estadoActual][i]
                   if numeroAleatorio < valor:
                       secEstados.append(modOculMarkov.estados[i])
                       secObservaciones.append(modOculMarkov.generaObservaciones(i))
                       estadoActual = i
                       break 
               print(secEstados,secObservaciones)
        return secEstados,secObservaciones


#Ejemplo pag. 28
# Lista: [Lluvia[lluvia, no-lluvia],No-lluvia[lluvia, no-lluvia]]        
A = [[0.7,0.3],[0.3,0.7]]
# Lista: [Lluvia[paraguas, no-paraguas], no-lluvia[paraguas, no-paraguas]]
B = [[0.9,0.1],[0.2,0.8]]
pi = [0.5,0.5]
estados = ['lluvia','no-lluvia']
observaciones = ['paraguas','no-paraguas']
prueba = modOculMarkov(A,B,pi,estados,observaciones)
posiblesObservaciones = ['paraguas','paraguas','no-paraguas']

#alpha = modOculMarkov.avance(prueba,posiblesObservaciones)
#estados = modOculMarkov.viterbi(prueba, posiblesObservaciones)
#print(estados)
secEstados,secObservaciones = modOculMarkov.muestreo(prueba, 3)
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 12:21:03 2017

@author: JM
"""

from markov import modOculMarkov
from modeloMarkov import cuadricula

a = cuadricula(5,5, 1/10)

print (a.tablero)
modelo = modOculMarkov(a.transiciones,a.sensor,a.pi,a.estados,a.observaciones)

###---- Prueba ------------
obs = ["SEO", "NO", "S"]
print('Avance', modOculMarkov.avance(modelo, obs))
print('Viterbi', modOculMarkov.viterbi(modelo, obs))
###--------------------------

###---- Valores ----------
print("Valor estados:", modelo.estados)
print("Valor pi:", modelo.probEstInicial)

secEstados,secObservaciones = modOculMarkov.muestreo(modelo, 2)
print('Secuencia observaciones', secObservaciones)
print('Secuencia estados original:',secEstados)
estEstados = modOculMarkov.viterbi(modelo, secObservaciones)
estado = modOculMarkov.avance(modelo, secObservaciones)
print('Secuencia estados estimada con viterbi:',estEstados)
print('Secuencia estado siguiente con avance:',estado)

print('Distancia Manhattan', a.evaluaAvance(secEstados[len(secEstados)-1],estado))
#print('Error viterbi', modOculMarkov.evaluaViterbi(secEstados,estEstados))

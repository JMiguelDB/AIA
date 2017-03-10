# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 17:52:12 2017

@author: JM
"""
import itertools

def readData(pathToFile, lect, limit):
    lista = []
    items = set()
    with open (pathToFile) as raw_data:
        for item in raw_data:
            #Procesamos los datos leidos y quitamos los dos ultimos espacios en blanco
            item = item.replace("\n"," ")
            line = item.split(" ")[:-2]
            #Tranformamos los valores a numeros
            lista.append(list(map(int, line)))
            items.update(map(int, line))
            if len(lista) == lect and limit == True:
                break
    return lista,sorted(items)

#Ejemplo de la pagina 25
def example():
    lista = [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]
    items = set([1,2,3,4,5])
    return lista,items


def conjuntoUnitario(bd,items,min_support):
    #Aplanamos la lista de transacciones
    lista = [x for sublist in bd for x in sublist] 
    #En funcion de las repeticiones de los elementos, añadimos el elemento
    L = [[i] for i in items if lista.count(i) >= min_support]
    return L

def generaCandidatos(L):
    C = []
    for conj1 in L:
        for conj2 in L:
            if conj1[:-1] == conj2[:-1]:
                val = sorted(list(set(conj1+conj2)))
                if conj1 != conj2 and val not in C:
                    C.append(val)
    return C

def filtraCandidatos(C,bd,min_support):
    L = []
    for conj1 in C:
        N = 0
        for conj2 in bd:
            if all(x in conj2 for x in conj1):
                N += 1
        if N >= min_support:
            L.append(conj1)
    return L

def Apriori(bd,items,min_support):
    L = []
    C = []
    k = 0
    L.append(conjuntoUnitario(bd,items,min_support))
    #print("L inicial", L)
    while len(L[k]) != 0:
        C = generaCandidatos(L[k])
        L.append(filtraCandidatos(C,bd,min_support))
        #print("C", C)
        #print("L", filtraCandidatos(C,bd,min_support))
        k += 1
    return L

def reglasAsociacion(L,bd,min_lift):
    reglas = []
    #Eliminamos los conjuntos unitarios y vacios
    del L[0]
    del L[-1]
    #Aplano la lista para iterar facilmente en cada conjunto
    L = [x for sublist in L for x in sublist] 
    #print(L)
    for c in L:
        for i in range(1,len(c)):   
            #Conseguimos todas las posibles combinaciones de cada conjunto frecuente
            antecedentes = list(itertools.combinations(c,i))
            for antecedente in antecedentes:
                conf = 0
                num = 0
                den = 0
                lift = 0
                antecedente = list(antecedente)
                #Obtenemos los elementos que no se encuentran como parte del consecuente
                consecuente = [x for x in c if x not in antecedente]
                conj = antecedente + consecuente
                for conj2 in bd:
                    if all(x in conj2 for x in conj):
                        num += 1
                    if all(x in conj2 for x in antecedente):
                        den += 1
                    if all(x in conj2 for x in consecuente):
                        lift += 1
                conf = num / den
                lift = conf / lift
                #Comprobamos si el lift es superior al minimo
                if lift >= min_lift:
                    #print(antecedente,consecuente, lift)
                    reglas.append([antecedente,consecuente])
    return reglas
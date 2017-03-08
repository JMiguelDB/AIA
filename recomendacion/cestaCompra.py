# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 17:52:12 2017

@author: JM
"""
import numpy as np

def readData(pathToFile):
    lista = []
    items = set()
    with open (pathToFile) as raw_data:
        for item in raw_data:
            item = item.replace("\n"," ")
            line = item.split(" ")
            lista.append(line)
            items.update(line)

    lista = np.array(lista)
    return lista,items
    
def read_data(path_file, max_transactions):
        items = set()
        transactions = list()
        
        for l in open(path_file, "r"):
            if max_transactions > 0 and len(transactions) > max_transactions:
                break
            l = l.replace('\n','')
            ''' Eliminamos el ultimo elemento, el cual es vacio '''
            d = l.split(' ')[:-1]
            '''print(d)'''
            transactions.append(d)
            items.update(d)
        return items, transactions
#print(read_data("retail.dat",0))
lista,items = readData("retail.dat")
print(lista)
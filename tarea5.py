import json
import csv


def csv(archivo):
	nombreTweet = []
	categoria = []	
	with open(archivo, mode='r') as input_file:
		for row in input_file:
			row = row.split(',')    
			nombreTweet = str ((row[2][1:-2]))
			cargaJson(nombreTweet)			
			categoria.append(str (row[1][1:-1]))			
		return categoria, nombreTweet

def cargaJson(nombreTweet):
	with open("rawdata/"+nombreTweet+".json") as json_data:
    		d = json.load(json_data)
    		print(d)

sentimientos,datos = csv("corpus.csv")

	


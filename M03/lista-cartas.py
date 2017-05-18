#coding:utf-8

def my_range(inicio,final,incremento):
	while inicio <= final:
		yield inicio
		inicio = inicio + incremento		
		
palo = ["1","2","3","4"]
numero = ["1","2","3","4","5","6","7","8","9","10","11","12","13"]
cont = 52

from random import randint

for palo in my_range(1,4,1):
	for numero in range(1,13,1):
			
		numero=randint(1,13)
		
		if (numero == 11):
			numero = "J"
			
		if (numero == 12):
			numero = "Q"
			
		if (numero == 13):
			numero = "K"
			
			
		palo=randint(1,4)
			
		if (palo == 1):
			palo = "D"
			
		if (palo == 2):
			palo = "T"
			
		if (palo == 3):
			palo = "P"
		
		if (palo == 4):
			palo = "C"
				
		print numero, palo
		
cont = cont - 1

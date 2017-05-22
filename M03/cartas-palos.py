


palo =["1","2","3","4"]
cartas =["1","2","3","4","5","6","7","8","9","10","11","12","13"]
cont = 52
from random import randint

for palo in range(1,5,1):
	for cartas in range(1,14,1):
		
		cartas = randint(1,13)
		
		if (cartas == 11):
			cartas = "J"
			
		if (cartas == 12):
			cartas = "Q"
			
		if (cartas == 13):
			cartas = "K"
		
		palo = randint(1,4)
			
		if (palo == 1):
			palo = "D"
			
		if (palo == 2):
			palo = "C"
			
		if (palo == 3):
			palo = "T"
		
		if (palo == 4):
			palo = "P"
				
		print cartas, palo
		
cont = cont - 1

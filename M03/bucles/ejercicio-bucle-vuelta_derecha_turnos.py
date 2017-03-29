#coding: utf8

num = 1
turno = 0
salir = False

while salir == False:

	if (num % 8 == 1) or (num % 8 == 2):
		print num , "-> Arriba"
		
	if (num % 8 == 3) or (num % 8 == 4):
		print num , "-> Derecha"
		
	if (num % 8 == 5) or (num % 8 == 6):
		print num , "-> Abajo"	
		
	if (num % 8 == 7) or (num % 8 == 0):
		print num , "-> Izquierda"
	
	if (num == 8):
		turno = turno + 1
		num   = 0		
	if (turno == 2):		
		salir = True
			
	num = num + 1

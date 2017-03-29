#coding: utf8
direccion = raw_input("A que dirección quieres ir, Derecha (D) o Izquierda (I)? ")
salir = False
num = 1

while salir == False:

	if (num % 8 == 1) or (num % 8 == 2):
		print num , "-> Arriba"
		
	if (num % 8 == 3) or (num % 8 == 4):
		if (direccion == "D") or (direccion == "d"):
			print num , "-> Derecha"
		else:
			print num , "-> Izquierda"
			
	if (num % 8 == 5) or (num % 8 == 6):
		print num , "-> Abajo"	
		
	if (num % 8 == 7) or (num % 8 == 0):
		if (direccion == "D") or (direccion == "d"):
			print num , "-> Izquierda"
		else:
			print num , "-> Derecha"
	if (num == 8):		
		salir = True
	num = num + 1

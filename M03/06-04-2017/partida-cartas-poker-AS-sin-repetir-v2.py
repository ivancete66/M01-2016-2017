# coding: utf8

from random import randint

salir = False
salir2 = False

while (salir == False):
#Creamos los palos para cada jugador
	j1palo = randint(1,4) 
	j2palo = randint(1,4)
#Asignamos los palos del jugador1
	if (j1palo == 1):
		palo1 = "Picas"
		
	if (j1palo == 2):
		palo1 = "Corazones"
		
	if (j1palo == 3):
		palo1 = "Diamantes"
		
	if (j1palo == 4):
		palo1 = "Tréboles"
#Creamos las cartas para ambos jugadores
	jugador1 = randint(2,14)
	jugador2 = randint(2,14)
#Convertimos los numeros 11, 12, 13 y 14 del jugador1 a sus valores verdaderos
	numero1 = jugador1
	if (jugador1 == 11):
		numero1 = "J"
		
	if (jugador1 == 12):
		numero1 = "Q"
		
	if (jugador1 == 13):
		numero1 = "K"
		
	if (jugador1 == 14):
		numero1 = "AS"
#Resultado del jugador1		
	print "Tienes un", numero1 , "de", palo1


	while (salir2 == False):
		#Si las cartas y los palos de los dos jugadores son iguales, se vuelven a generar las cartas y los palos 	
		if ((jugador1 == jugador2) and (j1palo == J2palo)):
			jugador2 = randint(2,14)
			j2palo = randint(1,4)
		#Si las cartas y los palos de los jugadores NO son iguales, sale del bucle y sigue con la partida	
		if not((jugador1 == jugador2) and (j1pal == j2palo)):
			salir2 = True
#Asignamos los palos del jugador2
	if (j2palo == 1):
		palo2 = "Picas"
		
	if (j2palo == 2):
		palo2 = "Corazones"
		
	if (j2palo == 3):
		palo2 = "Diamantes"
		
	if (j2palo == 4):
		palo2 = "Tréboles"
#Convertimos los numeros 11, 12, 13 y 14 del jugador2 a sus valores verdaderos
	numero2 = jugador2
	if (jugador2 == 11):
		numero2 = "J"
		
	if (jugador2 == 12):
		numero2 = "Q"
		
	if (jugador2 == 13):
		numero2 = "K"
		
	if (jugador2 == 14):
		numero2 = "AS"
#Resultado del jugador2		
	print "Tu rival tiene", numero2 , "de" , palo2
#Decimos el resultado final
	if (jugador1 == jugador2):
		print "Empate!"
		
	else:
		if ( jugador1 > jugador2):
			print "Has ganado!"	
		else:
			print "Has perdido!"
#Si las cartas de los jugadores NO son iguales salimos del bucle	
	if not(jugador1 == jugador2):
			salir = True

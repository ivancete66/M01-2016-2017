# coding: utf8

from random import randint

salir=False

while (salir==False):

	palo=randint(1,4)

	if (palo==1):
		palo1 = "Corazones"
		
	if (palo==2):
		palo1 = "Picas"
		
	if (palo==3):
		palo1 = "Diamantes"
		
	if (palo==4):
		palo1 = "Tréboles"
		

	palo=randint(1,4)
		
	if (palo==1):
		palo2 = "Corazones"
		
	if (palo==2):
		palo2 = "Picas"
		
	if (palo==3):
		palo2 = "Diamantes"
		
	if (palo==4):
		palo2 = "Tréboles"
		

	jugador1=randint(1,13)
	jugador2=randint(1,13)

		
	if (jugador1 == jugador2):
		print "Empate!"
	else:
		if (jugador1 > jugador2):
			if (jugador1==11):
				jugador1 = "J"
				
			if (jugador1==12):
				jugador1 = "Q"
				
			if (jugador1==13):
				jugador1 = "K"
				
			print "Tienes un", jugador1 , "de", palo1
			print "Tu contrincante tiene un", jugador2 , "de", palo2
			print "Has ganado!"
		else:
			if (jugador2==11):
				jugador2 = "J"
				
			if (jugador2==12):
				jugador2 = "Q"
				
			if (jugador2==13):
				jugador2 = "K"
				
			print "Tienes un", jugador1 , "de", palo1
			print "Tu contrincante tiene un", jugador2 , "de", palo2
			print "Has perdido, mala suerte!"
	
	if (jugador1 <> jugador2):
		salir = True

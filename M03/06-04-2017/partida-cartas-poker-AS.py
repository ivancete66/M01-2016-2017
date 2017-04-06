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
		

	jugador1=randint(2,14)
	jugador2=randint(2,14)

	numero=jugador1
	if (jugador1==11):
		numero = "J"
			
	if (jugador1==12):
		numero = "Q"
			
	if (jugador1==13):
		numero = "K"

	if (jugador1==14):
		numero = "AS"
			
	print "Tienes un", numero , "de", palo1
	
	numero=jugador2
	if (jugador2==11):
		numero = "J"
			
	if (jugador2==12):
		numero = "Q"
		
	if (jugador2==13):
		numero = "K"

	if (jugador2==14):
		numero = "AS"
			
	print "Tu contrincante tiene un", numero , "de", palo2
	
	if (jugador1 == jugador2):
		print "Empate!"
	else:
		if (jugador1 > jugador2):
			print "Has ganado!"
		else:
			print "Has perdido, mala suerte!"
			
	if (jugador1 <> jugador2):
		salir = True

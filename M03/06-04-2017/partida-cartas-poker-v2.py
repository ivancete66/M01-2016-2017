# coding: utf8

from random import randint

salir=False

while (salir==False):
#Creamos los randoms para los palos, lo hacemos dos veces, ya que hay 2 jugadores
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
		
#Creamos los randoms para las cartas, lo hacemos dos veces porque hay 2 jugadores
	jugador1=randint(2,14)
	jugador2=randint(2,14)
#Convertimos los numeros 11, 12, 13 y 14 a sus valores verdadores
	numero=jugador1
	if (jugador1==11):
		numero = "J"
			
	if (jugador1==12):
		numero = "Q"
			
	if (jugador1==13):
		numero = "K"

	if (jugador1==14):
		numero = "As"
#Mostramos el resultado del jugador1			
	print "Tienes un", numero , "de", palo1
	
	numero=jugador2
	if (jugador2==11):
		numero = "J"
			
	if (jugador2==12):
		numero = "Q"
		
	if (jugador2==13):
		numero = "K"

	if (jugador2==14):
		numero = "As"
#Mostramos el resultado del jugador2			
	print "Tu contrincante tiene un", numero , "de", palo2
#Decimos el resultado final	
	if (jugador1 == jugador2):
		print "Empate!"
	else:
		if (jugador1 > jugador2):
			print "Has ganado!"
		else:
			print "Has perdido, mala suerte!"
#  Si el resultado de los dos jugadores son diferentes, salimos del bucle y terminamos la partida,
#  sino, seguimos hasta que gane alguien
	if (jugador1 <> jugador2):
		salir = True

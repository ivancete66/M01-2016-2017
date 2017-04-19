#coding: utf-8

import os
from random import randint

credito = 100
tonto = 0

os.system('clear')

salir2 = False
salir = False
while salir == False:
	print "Tienes",credito,"€"
	print "Si quieres retirarte, pon -1"
	apuesta = input("Cuantos euros quieres apostar?: ")
	os.system('clear')
	
# condicióm de salida apuesta -1, sin credito o fallar 3 veces apuesta mínima	
	if apuesta == -1 or tonto == 3 :
		salir = True
	elif apuesta > credito :
		print "No se puede apostar tanto"
	
	elif apuesta < 10 :
		print "apuesa mínima es de 10"
		tonto = tonto +1
	
	else:
		if apuesta <= credito :		
						
			j1palo = randint(1,4) 
			j2palo = randint(1,4)

			if (j1palo == 1):
				palo1 = "Picas"
				
			if (j1palo == 2):
				palo1 = "Corazones"
				
			if (j1palo == 3):
				palo1 = "Diamantes"
				
			if (j1palo == 4):
				palo1 = "Tréboles"

			jugador1 = randint(2,14)
			jugador2 = randint(2,14)
			
			numero1 = jugador1
			if (jugador1 == 11):
				numero1 = "J"
				
			if (jugador1 == 12):
				numero1 = "Q"
				
			if (jugador1 == 13):
				numero1 = "K"
				
			if (jugador1 == 14):
				numero1 = "AS"
				
			print "Tienes un", numero1 , "de", palo1


			while (salir2 == False):
				
				if ((jugador1 == jugador2) and (j1palo == J2palo)):
					jugador2 = randint(2,14)
					j2palo = randint(1,4)
					
				if not((jugador1 == jugador2) and (j1pal == j2palo)):
					salir2 = True
			
			if (j2palo == 1):
				palo2 = "Picas"
				
			if (j2palo == 2):
				palo2 = "Corazones"
				
			if (j2palo == 3):
				palo2 = "Diamantes"
				
			if (j2palo == 4):
				palo2 = "Tréboles"
						
			numero2 = jugador2
			if (jugador2 == 11):
				numero2 = "J"
				
			if (jugador2 == 12):
				numero2 = "Q"
				
			if (jugador2 == 13):
				numero2 = "K"
				
			if (jugador2 == 14):
				numero2 = "AS"
					
			print "Tu rival tiene", numero2 , "de" , palo2

			if (jugador1 == jugador2):
				print "Empate!"
				
			else:
				if ( jugador1 > jugador2):
					print "Has ganado!"	
				else:
					print "Has perdido!"
			
			if not(jugador1 == jugador2):
					salir = True
			elif jugador1 > jugador2 :
			# gana jugador1 si elguna variable es mayor que 10 se le asigna la variable con catacter alfabetico.	
				if jugador1 > 10 :
					jugador1 = numero1
				if jugador2 > 10 :
					jugador2 = numero2
				print "tu:",jugador1,numero1,"Maquina:",jugador2,numero2," ¡¡Ganas tu!!"
				credito = credito + apuesta
							
			else:
			# pierde jugador1 si elguna variable es mayor que 10 se le asigna la variable con catacter alfabetico.
				if jugador1 > 10 :
					jugador1 = numero1
				if jugador2 > 10 :
					jugador2 = numero2
				print "tu:",jugador1,numero1,"Maquina:",jugador2,numero2," ¡¡Pierdes!!"
				credito = credito - apuesta				
			
			if credito < 10 :
				print "Lo siento, te has quedado sin dinero!"
salir = True

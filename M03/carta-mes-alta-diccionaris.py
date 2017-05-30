#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Juego de cartas en el que hay dos jugadores que se generan dos cartas aleatoriamente y el que tenga el número mas grande gana.

#importamos random para que lo haga aleatoriamente.
import random

salir= False

#Creamos las listas.
numeros=[1,2,3,4,5,6,7,8,9,10,"J","Q","K"]

palos=["D","C","T","P"]


while(salir==False):
	
#Random choice es para que te genere un numero al azar de la lista numeros y palos.
  
	jugador1=random.choice(numeros)
	jugador2=random.choice(numeros)
	
	palo1=random.choice(palos)
	palo2=random.choice(palos)
	

      
#Aqui calculamos quien gana y quien empata.
				
	if(jugador1==jugador2):
		
			print "¡Empate!"
			print "El jugador 1 tiene un", jugador1, "de", palo1
			print "EL jugador 2 tiene un", jugador2, "de", palo2
			print "HAS EMPATADO"
	else:
		if(jugador1 > jugador2):
		
			print "El jugador 1 tiene un", jugador1, "de", palo1
			print "EL jugador 2 tiene un", jugador2, "de", palo2
			print "¡Ha ganado el jugador 1!"
		else:	
			print "El jugador 1 tiene un", jugador1, "de", palo1
			print "EL jugador 2 tiene un", jugador2, "de", palo2
			print "¡Ha ganado el jugador 2!"
			
			salir=True


'''
#coding: utf-8

def my_range(inici, fi, increment):
    while inici <= fi:
        #Retorna l'element actual del rang (llista)
        yield inici
        inici = inici + increment

from random import randint 

#Definimos el diccionario
cartas = {'1':'1 D' , '2':'2 D' , '3':'3 D' , '4':'4 D' , '5':'5 D' , '6':'6 D' , '7':'7 D' , '8':'8 D' , '9':'9 D' , '10':'10 D' , '11':'J D' , '12':'Q D' , '13':'K D',
          '14':'1 T' , '15':'2 T' , '16':'3 T' , '17':'4 T' , '18':'5 T' , '19':'6 T' , '20':'7 T' , '21':'8 T' , '22':'9 T' , '23':'10 T' , '24':'J T' , '25':'Q T' , '26':'K T',
          '27':'1 P' , '28':'2 P' , '29':'3 P' , '30':'4 P' , '31':'5 P' , '32':'6 P' , '33':'7 P' , '34':'8 P' , '35':'9 P' , '36':'10 P' , '37':'J P' , '38':'Q P' , '39':'K P',
          '40':'1 C' , '41':'2 C' , '42':'3 C' , '43':'4 C' , '44':'5 C' , '45':'6 C' , '46':'7 C' , '47':'8 C' , '48':'9 C' , '49':'10 C' , '50':'J C' , '51':'Q C' , '52':'K C',
          }

cartas1 = randint(1,52)
	if cartas1=52:

cartas2 = randint(1,52)
print cartas1
print cartas2
'''

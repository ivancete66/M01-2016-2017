#coding: utf-8
j1 = raw_input("Elige una opción Jugador 1: piedra, papel o tijera: ")
j2 = raw_input("Elige una opción Jugador 2: piedra, papel o tijera: ")

if (j1 == "piedra") and (j2 == "papel"):
	print "Gana el Jugador 2"
		
if (j1 == "piedra") and (j2 == "piedra"):
	print "Hay un empate"
	
if (j1 == "piedra") and (j2 == "tijera"):
	print "Gana el Jugador 1"
	
		
if (j1 == "papel") and (j2 == "papel"):
	print "Hay un empate"
	
if (j1 == "papel") and (j2 == "piedra"):
	print "Gana el Jugador 1"
	
if (j1 == "papel") and (j2 == "tijera"):
	print "Gana el Jugador 2"
	
	
if (j1 == "tijera") and (j2 == "papel"):
	print "Gana el Jugador 1"
	
if (j1 == "tijera") and (j2 == "piedra"):
	print "Gana el Jugador 2"
	
if (j1 == "tijera") and (j2 == "tijera"):
	print "Hay un empate"
	

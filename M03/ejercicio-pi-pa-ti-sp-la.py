# coding:utf-8
# Possibilitats: PE, PA, TI, LA, SP
# Total 25: 5 empat, 20 guanyador
# jugador1 humà
# jugador2 machine

from random import randint

#Jugador 1 humà
jugador1=raw_input("Possi la jugada (Piedra/Papel/Tijera/Spock/Lagarto):")

#Jugador 2 machine
aleatori=randint(1,5)
if (aleatori == 1):
	jugador2 = "Piedra"
	
if (aleatori == 2):
	jugador2 = "Papel"
	
if (aleatori == 3):
	jugador2 = "Tijera"
	
if (aleatori == 4):
	jugador2 = "Lagarto"
	
if (aleatori == 5):
	jugador2 = "Spock"
	
print "La meva jugada es:" , jugador2

# Empat (5 combinacions)
if (jugador1==jugador2):
	print "Empat"
else:
	if 	( (jugador1 == "Piedra")  and ((jugador2=="Lagarto" or jugador2=="Tijera")) or 
		  (jugador1 == "Papel")   and ((jugador2=="Piedra" or jugador2=="Spock"  )) or
		  (jugador1 == "Tijera")  and ((jugador2=="Papel" or jugador2=="Lagarto" )) or
		  (jugador1 == "Lagarto") and ((jugador2=="Papel" or jugador2=="Spock"   )) or
		  (jugador1 == "Spock")   and ((jugador2=="Piedra" or jugador2=="Tijera"))
		):
		
		print "Has ganado!"
	else:
		print "Has perdido!"































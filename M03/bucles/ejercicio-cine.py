#coding: utf8

num = 1
sortir = False

while sortir == False:
	if (num % 2 == 0):
		print "M"
	
	if (num % 3 == 0):
		print "X → Dia de l'espectador"
		
	if (num % 4 == 0):
		print "J → Dia de l'espectador"
	
	if (num % 5 == 0):
		print "V → Día normal"
		
	if (num % 6 == 0):
		print "S → Sessió golfa"
		
	if (num == 28):
		sortir = True
		
	num = num +1

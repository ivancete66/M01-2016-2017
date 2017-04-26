#coding: utf8
numero = 1
total = 0
for numero in range(1,6):
	if (numero % 2 == 0):
		print " ",numero
		total = total + numero
	if (numero == 5):
		print "-----"
		print " ",total

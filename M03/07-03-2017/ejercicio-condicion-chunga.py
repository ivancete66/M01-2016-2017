#coding: utf8

numero=input("Introduce un número: ")

if (numero % 2 == 0):
	print "Éste número es par."
if (numero >= -10 and numero <= 40):
	print "Éste número está entre -10 y 40."
if (numero % -2 == 0 and numero % -1 == 0):
	print "Éste número és negativo."

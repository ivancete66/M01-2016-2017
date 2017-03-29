#!/usr/bin/python
# coding: utf8

num = input("Es un numero primo o no? ")
contador = num
total = 0
Sortir = False

if (num == 0):
	Sortir = True
	
while Sortir == False:
	if (num % contador == 0 ):
		total = total + 1
	contador = contador - 1
	if (contador == 0):
		Sortir = True
	
if total == 2:
	print "Es primo"
	Sortir = True
else: 
	print "No es primo"

#coding: utf8
import os
os.system('clear')

valor1 = input("Escribe un numero: ")
valor2 = input("Escribe otro numero: ")

if valor1 > valor2:
	print "El número" , valor1 , "es más grande que el número" , valor2
else:
	if valor1 == valor2:
		print "Los dos números son iguales."
	else:
		print "El número" , valor2 , "es más grande que el número" , valor1

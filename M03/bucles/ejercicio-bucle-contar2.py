#coding: utf8
numero = 1
final = input("Introduce el final del contador: ")
salir = False
while salir == False:
	print numero
	if (numero == final):
		salir = True
	numero = numero + 1

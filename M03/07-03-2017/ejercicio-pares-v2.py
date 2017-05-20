# coding: utf8
#Le decimos que introduzca un número
numero=input("Introduce un número: ")
#Si el numero es par, es muy bonito
if numero % 2 == 0:
	print numero,", qué número par más bonito!"
else: #Si el numero no es par, es muy vulgar
	print numero, ", qué número más vulgar..."

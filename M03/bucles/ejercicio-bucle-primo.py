#coding: utf8

num = input("Introduce un número: ")
cont = num
cero = 0
salir = False
	
while salir == False:
	if (num % cont == 0):
		cero = cero + 1
	cont = cont - 1
	if (cont == 0):
		salir = True
	
if (cero == 2):
	print "Éste número es primo."
else:
	print "Éste número no es primo."

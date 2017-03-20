#coding: utf8
import os
os.system('clear')
salir = False
while salir == False:
	#os.system('clear')
	print 'Que desea hacer el amo?'
	print 'S.- Salir'
	print '1.- Sumar'
	print '2.- Restar'
	print '3.- Multiplicar'
	print '4.- Dividir'

	opcion = raw_input("Elija una opcion: ")

	if (opcion >= "1" and opcion <= "4"):
		print "Está bien."
		tecla = raw_input("Presiona una tecla para continuar.")
	if (opcion == 's' or opcion == 'S'):
		print "Adiós!"
		salir = True
	else:
		print "Esa opción no existe."
		tecla = raw_input("Presiona una tecla para continuar.")

os.system = clear
print 'Que desea hacer el amo?'
print '1.- Sumar'
print '2.- Restar'
print '3.- Multiplicar'
print '4.- Dividir'
print '5.- Salir'

opcion = input("Elija una opcion:  ")


numero1=input("Introduce un numero:    ")
numero2=input("Introduce otro numero:  ")

if opcion == '1':
	sumar = numero1 + numero2
	print "El resultado es: ", sumar

if opcion == '2':
	restar = numero1 - numero2
	print "El resultado es: ", restar

if opcion == '3':
	multiplicar = numero1 * numero2
	print "El resultado es: ", multiplicar

if opcion == '4':
	dividir = numero1 / numero2
	print "El resultado es: ", dividir

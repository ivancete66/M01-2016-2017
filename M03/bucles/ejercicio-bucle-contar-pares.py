#coding: utf8
num = 1
final = input("Introduce un numero: ")
salir = False
while salir == False:
	print num
	if (num % 2 == 0):
		salir = True
	num=num+1

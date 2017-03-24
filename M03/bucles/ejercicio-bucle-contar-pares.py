#coding: utf8
num = 1
final = input("Introduce un numero: ")
salir = False
while salir == False:
	if (num % 2 == 0):
		print  num
	if (num == final):
		salir = True
	num=num+1

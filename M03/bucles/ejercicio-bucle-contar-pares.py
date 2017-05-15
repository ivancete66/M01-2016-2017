#coding: utf8
num = 1
final = input("Introduce un numero: ")
salir = False
while salir == False:
	#Los numeros que sean pares los imprime
	if (num % 2 == 0):
		print  num
	#Cuando el número sea igual que el final, saldrá del bucle
	if (num == final):
		salir = True
	num=num+1

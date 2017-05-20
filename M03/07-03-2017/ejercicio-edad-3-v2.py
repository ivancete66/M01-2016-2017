#coding: utf8 
#Le decimos que ponga si edad
edad=input("Introduce tu edad: ")
#Si la edad está entre 18 y 23 incluidos,es 17 o está entre 65 y 72 puede entrar
if (edad >= 18 and edad <= 23) or edad == 17 or (edad >= 65 and edad <= 72): 
	print "Puedes entrar a la sesión de jóvenes!"
else: #Sino atrás!
	print "Atrás Satanás!!!!"

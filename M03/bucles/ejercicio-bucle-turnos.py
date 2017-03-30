#coding: utf8
salir = False
turno = 0
vueltas = 1
while salir == False:
	print vueltas , turno
	if (vueltas % 8 == 0):
		turno = turno + 1
	if (turno == 2):		
		salir = True
	vueltas = vueltas + 1

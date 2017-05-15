#coding:utf-8

def my_range(inicio,final,incremento):
	while inicio <= final:
		yield inicio
		inicio = inicio + incremento
		
cont = 1
		
for col in my_range (1,dia_semana-1,1):
	print " "
for col in my_range (dia_semana,7,1):
	print cont
	cont = cont + 1

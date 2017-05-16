#coding:utf-8

def my_range(inicio,final,incremento):
	while inicio <= final:
		yield inicio
		inicio = inicio + incremento

dia_semana = 2
num_dias_mes = 30
				
cont = 1
print "L M X J V S D"		
for col in my_range (1,dia_semana-1,1):
	print " ",
for col in my_range (dia_semana,7,1):
	print cont,
	cont = cont + 1
	
print ""
	
for fil in my_range (1,5,1):
	for col in my_range (1,7,1):
		if (cont <= num_dias_mes):
			print cont,
		else:
			print " ",
		cont = cont + 1
	print ""

#coding:utf-8

def my_range(inicio,final,incremento):
	while inicio <= final:
		yield inicio
		inicio = inicio + incremento

#Establecemos la lista
notas=["Do", "Re", "Mi", "Fa", "Sol", "La", "Si", "DO", "RE"]

print ""
#Iniciamos el bucle que devuelve todas las notas
print "Todas las notas:"
for nota in my_range (0,8,1):
	print notas[nota],

print ""
print ""	
	
#Insertar la siguiente nota (MI) 
print "Insertamos la nota MI (con append):"
notas.append("MI")
for nota in my_range (0,9,1):
	print notas[nota],

print ""
print ""


#Insertar la siguiente nota (la que viene después de MI (FA))
print "Insertamos la nota FA (con insert):"
notas.insert(10,"FA")
for nota in my_range (0,10,1):
	print notas[nota],

print ""
print ""
	
#Borramos la nota Sol
print "Borramos la nota Sol:"
notas.remove("Sol")
for nota in my_range (0,8,1):
	print notas[nota],
print ""
print ""

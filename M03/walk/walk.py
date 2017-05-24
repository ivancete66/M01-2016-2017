# !/usr/bin/python
# coding:utf-8
import os
 
explorar="./futbol/"
print " " 
# Mostrem només els arxius de la carpeta futbol
print "Mostrem només els arxius de la carpeta futbol:"
print ""
for root, carpetes, arxius in os.walk(explorar):
    for nom in arxius:
        print(nom)
print "" 
print "------------------------------"
print ""

# Mostrem només els directoris que hi han dins de la carpeta Futbol
print "Mostrem només els directoris que hi han dins de la carpeta Futbol:"
print ""
for root, carpetes, arxius in os.walk(explorar):
    for nom in carpetes:
        print(nom)
print ""      
print "------------------------------"
print ""

# Mostrem tot el que hi ha dins de la carpeta Futbol
print "Mostrem tot el que hi ha dins de la carpeta Futbol:"
print ""
for root, carpetes, arxius in os.walk(explorar):
    for nom in carpetes:
        print(nom)
        
    for nom in arxius:
        print(nom)
print ""        
print "------------------------------"
print ""

# Mostrem la ruta dels arxius
print "Mostrem la ruta dels arxius:"
print ""
for root, carpetes, arxius in os.walk(explorar):
    for nom in arxius:
        ruta=os.path.join(root, nom)
        print(ruta)
print ""        
print "------------------------------"
print ""
# Mostrem ruta de tot el que hi ha dins de la carpeta Futbol
print "Mostrem ruta de tot el que hi ha dins de la carpeta Futbol:"
print ""
for root, carpetes, arxius in os.walk(explorar):
	for nom in arxius:    
		ruta=os.path.join(root, nom)
		print(ruta)

	for nom in carpetes:
		ruta=os.path.join(root, nom)
		print(ruta) 


# Canviem els permissos dels arxius
#print "Canviem els permissos dels arxius:"
#print ""
#for root, carpetes, arxius in os.walk(explorar):
 #   for nom in arxius:
	#	permisos=os.chmod(arxius, permisos)
	#	print ()

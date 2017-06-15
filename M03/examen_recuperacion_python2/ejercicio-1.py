# !/usr/bin/python
# coding:utf-8

import os
 
######################################
#		Funciones y acciones		 #
######################################

def imprimir_nom(nom):
	print nom
	
def imprimir_espacios():
	print "" 
	print "------------------------------"
	print ""

######################################
#			  Variables				 #
######################################

explorar="../walk/futbol/"

######################################
#			  Código 	 			 #
######################################

# Mostrem només els arxius de la carpeta futbol
print "Mostrem només els arxius de la carpeta futbol:"
print ""
for root, carpetes, arxius in os.walk(explorar):
    for nom in arxius:
        imprimir_nom(nom)

imprimir_espacios()

# Mostrem només els directoris que hi han dins de la carpeta Futbol
print "Mostrem només els directoris que hi han dins de la carpeta Futbol:"
print ""
for root, carpetes, arxius in os.walk(explorar):
    for nom in carpetes:
        imprimir_nom(nom)
               
imprimir_espacios()

# Mostrem la ruta dels arxius
print "Mostrem la ruta dels arxius:"
print ""
for root, carpetes, arxius in os.walk(explorar):
    for nom in arxius:
        ruta=os.path.join(root, nom)
        print ruta

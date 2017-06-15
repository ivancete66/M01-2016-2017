#!/usr/bin/python
#coding:utf-8

import os
import stat

######################################
#		Funciones y acciones		 #
######################################

def obtener_tamanyo(ruta):
	tamanyo_archivo=os.stat(ruta).st_size
	return tamanyo_archivo
	
def imprimir_total(archivos):
	print "Se han eliminado" , archivos , "archivos."
	

######################################
#			  Variables				 #
######################################

tamanyo_archivo = input("Introduce el tamaño máximo: ")
ruta_origen = raw_input("Introduce la ruta de los ficheros: ")
archivos = 0
comando = os.system('rm -f ')

######################################
#			  Código 	 			 #
######################################


for root, carpetes, arxius in os.walk(ruta_origen):
    for nom in arxius:
		ruta=os.path.join(root,nom)
		tamany=obtener_tamanyo(ruta)
		if (tamany <=tamanyo_archivo):
			comando
			archivos = archivos + 1
		print root , nom
imprimir_total(archivos)

#!/usr/bin/python
#coding: utf-8

import os
import stat
import time

directorios=0
archivos=0
explorar = "./walk/futbol"

for root,dirs,files in os.walk(explorar):
	
	for nom in dirs:
		ruta=os.path.join(root,nom)
		print ""
		print ruta
		print ""
		directorios = directorios + 1
		
	for nom in files:
		ruta=os.path.join(root,nom)
		tamany=os.stat(ruta).st_size		
		fecha=time.ctime(os.path.getmtime(ruta))
		print ""
		print ruta
		print "Tamaño ->" , tamany , "Bytes"
		print fecha
		print ""
		archivos = archivos + 1
print ""
print "Nº total de directorios: " , directorios
print "Nº total de archivos: " , archivos
print ""

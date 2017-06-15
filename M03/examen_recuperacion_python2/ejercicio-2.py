# !/usr/bin/python
# coding:utf-8

import os
import stat

# Ruta para explorar
explorar="../walk/futbol/"

for root, carpetas, archivos in os.walk(explorar):
    for nombre in archivos:
		
		# Ruta del archivo
        ruta=os.path.join(root, nombre)
        print ""
        
        # Imprimimos la ruta del archivo
        print ruta
        
        # Averiguamos los permisos que tienen los archivos
        permissions = stat.S_IMODE ( os.stat (ruta).st_mode )
        
        # Pasamos los permisos a octales
        permisos = oct(permissions)
        
        # Para que nos de el segundo número y saber si groups tienen permisos hacemos "substring" 
        groups = permisos[2:3],
        
        # Hacemos la condición para saber si tienen permisos 
        if not(groups == "0"):
			print "El fichero" , nombre ,  ", no tiene permisos para 'groups'."

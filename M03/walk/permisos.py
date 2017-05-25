# !/usr/bin/python
# coding:utf-8

import os
import stat

# Ruta per a explorar
explorar="./futbol/"
   
for root, carpetes, arxius in os.walk(explorar):
    for nom in arxius:
		
		# Possem la ruta de l'arxiu
        ruta=os.path.join(root, nom)
        print ""
        print ""
        # Imprimim la ruta de l'arxiu
        print ruta
        
        # Averigüem els permisos que tenen els arxius i els pasem a octals  
        permissions = stat.S_IMODE ( os.stat (ruta).st_mode )
        permisos = oct(permissions)
        
        # Ara fem un "substring" per a que ens doni l'últim número i saber si others tenen permisos. 
        others = permisos[3:4],
        
        # Fem la condició per veure si en els arxius, els others tenen permisos. 
        if not(others == "0"):
			print "Per el fitxer" , nom ,  ", 'others' SI que tenen permissos."

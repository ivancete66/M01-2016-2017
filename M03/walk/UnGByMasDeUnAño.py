# !/usr/bin/python
# coding:utf-8

import os
import stat
import time

# Ruta per a explorar
explorar = "./futbol/"

# Dia que estem
avui = int(time.strftime("%y"))
        
for root, carpetes, arxius in os.walk(explorar):
    for nom in arxius:
		
		# Posem la ruta de l'arxiu
        ruta = os.path.join(root, nom)
        
        # Pes del fitxer
        pes_total = os.stat(ruta).st_size

        # Amb això, sabrem l'últim dia d'accés a l'arxiu
        temps = time.ctime(os.path.getatime(ruta))
        
        # Agafem les 4 últimes xifres de la variable temps
        temps_any = temps[20:24]
        
        # Restem la data d'avui per la de l'any
        temps_final = int(avui) - int(temps_any)
        
        # Ara fem la condició de que el tamany ha de ser major de 1 GB i l'últim accés abans d'1 any
        if (pes_total > 2**30) and (temps_final >= 1 or temps_final < 0):
			print ruta , "  " ,
			print pes_total , "Bytes", "  "
			print "Últim accés: "
			print temps
			print "  "
			
# Per comprovar-ho, he fet aquest altre bucle
'''
for root, carpetes, arxius in os.walk(explorar):
    for nom in arxius:
		
		# Posem la ruta de l'arxiu
        ruta = os.path.join(root, nom)
        # Pes del fitxer
        pes_total = os.stat(ruta).st_size

        temps = time.ctime(os.path.getatime(ruta))
        temps_any = temps[9:11]
        
        temps_final = int(temps_any) - int(2)         
		
        if (pes_total > 2**0) and (temps_final <= 30):
			print ruta , "  " ,
			print pes_total , "Bytes", "  "
			print "Últim accés: "
			print temps
			print "  "
'''
			
			

# !/usr/bin/python
# coding:utf-8
import os
import time 
ruta_a_explorar="./futbol/"
 
 
for ruta, directorios, archivos in os.walk(ruta_a_explorar):
    for nombre in archivos:
        ruta_completa=os.path.join(ruta, nombre)
        print(ruta_completa)
        print ""
        print time.ctime(os.path.getmtime(ruta_completa))
 
    for nombre in directorios:            
        ruta_completa=os.path.join(ruta, nombre)
        print(ruta_completa)
        print ""
        print time.ctime(os.path.getmtime(ruta_completa))


        
'''        
def getOldDirs(self, dirPath, olderThanDays):
    """
    return a list of all subfolders under dirPath older than olderThanDays
    """
    dias *= 86400 # convert days to seconds (60 days)
    present = time.time()
    for ruta, directorios, archivos in os.walk(futbol, topdown=False):
        for nombre in directorios:
            subDirPath = os.path.join(root, name)
            if (present - os.path.getmtime(subDirPath)) > dias:
                yield subDirPath
'''
'''
import datetime
import os.path, time

today = datetime.datetime.now()
day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1
#print day_of_year
ruta = "./futbol/*"
print "Ultima Modificacion: %s" % time.ctime(os.path.getmtime(ruta))
print "Creado: %s" % time.ctime(os.path.getctime(ruta))                
'''                
                
                
                
                
                
                
                
                
                
                
                
                
                
                

# coding: utf8

num = 31
salir = False
while salir == False:
	
	if (num % 7 == 0) or (num % 7 == 1):
		j1 = "ti"
	if (num % 7 == 2) or (num % 7 == 3) or (num % 7 == 6):
		j1 = "pi"
	if (num % 7 == 4) or (num % 7 == 5):
		j1 = "pa"
	if (num % 5 == 0) or (num % 5 == 1) or (num % 5 == 2):
		j2 = "pa" 
	if (num % 5 == 3):
		j2 = "ti" 
	if (num % 5 == 4):
		j2 = "pi"

	if (j1 == "pi" and j2 == "ti"):
		print num,"--> J1 =",j1,"y J2 =",j2,"= Gana el jugador 1"

	if (j1 == "pa" and j2 == "pi"):
		print num,"--> J1 =",j1,"y J2 =",j2,"= Gana el jugador 1"
  
	if (j1 == "ti" and j2 == "pa"):
		print num,"--> J1 =",j1,"y J2 =",j2,"= Gana el jugador 1"


	if (j2 == "pi" and j1 == "ti"):
		print num,"--> J1 =",j1,"y J2 =",j2,"= Gana el jugador 2"
  
	if (j2 == "pa" and j1 == "pi"):
		print num,"--> J1 =",j1,"y J2 =",j2,"= Gana el jugador 2"
  
	if (j2 == "ti" and j1 == "pa"):
		print num,"--> J1 =",j1,"y J2 =",j2,"= Gana el jugador 2"


	if (j1 == j2):
		print num,"--> J1 =",j1,"y J2 =",j2,"= Empate"
  
	if (num == 57):
		salir=True
  
	num = num + 1

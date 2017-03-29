#coding: utf8
num = 1
sortir = False
while sortir == False:
	print num
	
	if (num % 7 == 0):
		print "Yupi"
		
	if (num == 21):
		sortir = True
		
	num = num +1

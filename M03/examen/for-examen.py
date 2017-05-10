#coding:utf-8

for fil in xrange(1,5,1):
	for col in xrange(1,9,1):
		if (fil == 1) or (fil == 4):
			print "*",		
		else: 
			if (col == 1) or (col == 8):
				print "*",
			else: 
				if ( (col == 4) or (col == 5) )  and  (fil == 2):
					print ".",
				else:
					if (fil == 3) and  (col == 4):
							print "\\",
					else: 
						if (fil == 3) and  (col == 5):
							print "/",
						else: 
							print " ", 
	print ""

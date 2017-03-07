#!bin/bash

clear

echo "Introduce un valor"

read a


	if 		[ "$a" -lt 5  ] 
		then
		echo "Aquest valor és menor que 5."
	fi 
	
	

	if 		[ "$a" -ge 5  ] && [ "$a" -le 8 ] 
		then
		echo "Aquest valor està entre els números 5 i 8 inclosos."
	fi 
	
	
	
	if 		[ "$a" -eq 9  ]
		then
		echo "Aquest valor és igual que 9."
	fi 
	
	

	if 		[ "$a" -ne 9  ]
		then
		echo "Aquest valor és diferent a 9."
	fi 
	
	

	if 		[ "$a" -gt 9  ]
		then
		echo "Aquest valor és major que 9."
	fi 

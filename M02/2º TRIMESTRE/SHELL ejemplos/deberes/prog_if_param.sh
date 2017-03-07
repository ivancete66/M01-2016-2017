#!/bin/bash

clear

	if 		[ "$1" -eq 1 ] || [ "$2" -eq 1 ]
			then
			echo "Un dels paràmetres és 1."
	fi
	
	

	if 		[ "$1" -eq 7 ] && [ "$2" -eq 7 ]
			then
			echo "El número 7 està entre aquests dos paràmetres."
	fi
	
	

	if 		[ "$1" -ne 7 ] && [ "$2" -ne 7 ]
			then
			echo "Cap dels dos paràmetres val 7."
	fi
	
	

	if 		[ "$1" -gt 10 ] && [ "$2" -gt 10 ]
			then
			echo "Els dos paràmetres valen més de 10."
	fi


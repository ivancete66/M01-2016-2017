#!/bin/bash

clear
while true
do
	echo "1-Día De Nacimiento 2-Mis Años 3-Instituto Que Estudié 4-Salir"
	read tecla
	case $tecla in
		1) echo "29-02-2000"
		;;
		2) echo "16"
		;;
		3) echo "Narcís Monturiol"
		;;
		4) clear
		   exit 
	esac
done

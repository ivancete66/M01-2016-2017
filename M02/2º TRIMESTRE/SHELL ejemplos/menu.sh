#!/bin/bash
#Menu
clear
while true
do
	echo "1- 2- 4- 5-Salir"
	read tecla
	case $tecla in
		1) echo "Has apretado la tecla 1"
		;;
		2) echo "Has apretado la tecla 2"
		;;
		5) exit 0
		;;
	esac
done

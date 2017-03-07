#!/bin/bash

clear

# diasemana.sh: nombres de los días de la semana
# pasar un parametro con número del 0 al 6; 0 es domingo


echo ""
echo "Mostramos el resultado del IF v1.0: "
if [ $1 = "" ] 
	then
	echo Pasa un parametro! Debes indicar un número de 0 a 6
else 
	if [ $1 -eq 0 ] 
		then
		echo Domingo
	fi 
	if [ "$1" -le 1 ] && [ "$1" -ge 1 ]
		then
		echo Lunes
	fi 
	if [ "$1" -gt 1 ] && [ "$1" -lt 3 ]
		then
		echo Martes
	fi 
	if [ "$1" = "3" ] || [ "$1" -eq 3 ]
		then
		echo Miércoles
	fi 
	if [ "$1" = "4" ] 
		then
		echo Jueves
	fi 
	if [ "$1" = "5" ] 
		then
		echo Viernes
	fi 
	if [ "$1" = "6" ] 
		then
		echo Sábado
	fi 
	if [ "$1" -ge 7 ]
		then
		echo Te has pasado! Sólo números entre 0-6
	fi

fi

echo ""
echo "Mostramos el resultado del IF v2.0: "
if [ "$1" = "" ] 
	then
	echo Pasa un parametro! Debes indicar un número de 0 a 6
else 
	if [ "$1" = "0" ] || [ "$1" = "1" ] || [ "$1" = "2" ] || [ "$1" = "3" ] || [ "$1" = "4" ] || [ "$1" = "5" ] || [ "$1" = "6" ]
		then
		echo Has introducido un valor entre 0 - 6
	else
		echo Has introducido un valor diferente a 0 - 6	
	fi 
	
fi
echo ""



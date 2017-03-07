#!/bin/bash

#   estacion.sh
#   indica la estación del año aproximada según el mes
#

clear 

case $1 in 

  diciembre|enero|febrero)
	echo Invierno
  ;;
  
  marzo|abril|mayo)
     	echo Primavera
  ;;
  
  junio|julio|agosto)
     echo Verano
  ;;
  
  setiembre|octubre|noviembre)
     echo Otono
  ;;

  *) #sino paso ningún parametro entrará aquí
     echo Pasa un parámetro al script, un mes en minúscula
  ;;
  
esac
# fin estacion.sh

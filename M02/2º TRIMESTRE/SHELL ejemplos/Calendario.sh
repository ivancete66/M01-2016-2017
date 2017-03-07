#!/bin/bash
# diasemana.sh: nombres de los días de la semana
  #   invocar con número del 0 al 6; 0 es domingo
  case $1 in
  0)   echo Domingo;;
  1)   echo Lunes;;
  2)   echo Martes;;
  3)   echo Miércoles;;
  4)   echo Jueves;;
  5)   echo Viernes;;
  6)   echo Sábado;;
  *)   echo Debe indicar un número de 0 a 6;;
  esac

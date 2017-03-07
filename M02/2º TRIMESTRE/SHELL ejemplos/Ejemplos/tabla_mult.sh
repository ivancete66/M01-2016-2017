#!/bin/bash
clear

echo "Escriba un numero: "
	read a
echo

echo "La tabla de multiplicar de dicho numero es: "
echo

for b in 1 2 3 4 5 6 7 8 9 10
do
	resultado=`expr $a "*" $b`
	echo "$a X $b=" $resultado
done

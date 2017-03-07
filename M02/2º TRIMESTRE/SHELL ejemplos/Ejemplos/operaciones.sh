#!/bin/bash

clear 

### EJEMPLOS CON OPERACIONES ###
echo "-- Ejemplo con una multiplicación -> \* --"

echo -n "Introduce un valor:"
	read var1

echo -n "Introduce otro valor:"
	read var2
resultado=`expr $var1 \* $var2`

echo "El resultado de la multiplicacion es: "$resultado
echo ""

echo "-- Ejemplo con la expresión RANDOM --"
echo -n "Introduce un valor del 0 - 100: "
	read var3
	var4=`expr $RANDOM % $var3`
	echo -n "Un numero aleatorio según tu numero es: "$var4
echo ""
echo ""









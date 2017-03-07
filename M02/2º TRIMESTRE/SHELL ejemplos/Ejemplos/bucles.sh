#!/bin/bash

clear 

### BUCLES FOR ###
echo "-- Ejemplo bucle for (con seq) --"
for i in `seq 1 5`;
do
    echo $i
done  
echo ""

echo "-- Ejemplo bucle for (for clasico) --"
for (( i=0; i<=5; i++))
do
    echo $i
done
echo ""

echo "-- Ejemplo bucle for (listamos ficheros)--"
for i in $( ls ); do
      echo item: $i
done
echo ""
    
### BUCLE WHILE ###  
echo "-- Ejemplo bucle while --"  
CONTADOR=0
while [  $CONTADOR -lt 5 ]; do
       echo El contador es $CONTADOR
       let CONTADOR=CONTADOR+1 
done    
echo ""

### BUCLE UNTIL ###  
echo "-- Ejemplo bucle until --" 
CONTADOR=10
until [  $CONTADOR -lt 5 ]; do
        echo CONTADOR $CONTADOR
        let CONTADOR-=1
done
echo ""
        

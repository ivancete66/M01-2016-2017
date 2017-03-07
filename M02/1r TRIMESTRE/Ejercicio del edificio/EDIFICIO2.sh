#!/bin/bash

rm -rf Planta_1
rm -rf Planta_2
rm -rf Planta_3
rm -rf Atico
clear

#Ahora vamos a crear las plantas del edificio.
#mkdir Planta_1
#mkdir Planta_2
#mkdir Planta_3
#mkdir Atico

#Ahora iremos a cada planta y crearemos dos pisos para cada una y llevaremos una persona para cada piso A.
#cd Planta_1
#mkdir Piso_1A
#mkdir Piso_1B
#cd Piso_1A
#touch Persona_1
#cd ../../
#cd Planta_2
#mkdir Piso_2A
#mkdir Piso_2B
#cd Piso_2A
#touch Persona_3
#cd ../../
#cd Planta_3
#mkdir Piso_3A
#mkdir Piso_3B
#cd Piso_3A
#touch Persona_5
#cd ../../
cd Atico
mkdir Atico_A
mkdir Atico_B
cd Atico_A
touch Persona_7
cd ../../

#Ahora clonaremos a las Personas al otro piso que hay en su planta.
cp Planta_1/Piso_1A/Persona_1 Planta_1/Piso_1B/Persona_2
cp Planta_2/Piso_2A/Persona_3 Planta_2/Piso_2B/Persona_4
cp Planta_3/Piso_3A/Persona_5 Planta_3/Piso_3B/Persona_6
cp Atico/Atico_A/Persona_7 Atico/Atico_B/Persona_8

#Seguidamente creamos un BAR a la misma altura que el EDIFICIO
cd ..
mkdir BAR

#Ahora moveremos a las personas que hay en el atico al BAR.
mv Atico/Atico_A/Persona_7 ../BAR
mv Atico/Atico_B/Persona_8 ../BAR

tree Documents/M02/"Ejercicio del edificio"

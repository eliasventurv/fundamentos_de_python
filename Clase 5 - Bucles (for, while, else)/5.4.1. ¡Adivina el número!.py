'''
Clase:        Fundamentos de programación
Tema:         Bucles for y while
Ejercicio:    5.4.1. ¡Adivina el número!
Descripción:  Genera un número al azar y da múltiples intentos al usuario para adivinarlo.

Autor:        Elías Josué Ventura Villatoro
Fecha:        2025-05-29
Estado:       [ Terminado ]
'''

import random as rn

numero = rn.randint(1,100)
confirmador = False

while confirmador == False:
    try:
        respuesta = int(input("Ingresa un número entre 1 y 100: "))
    except:
        print("El número introducido no es válido.")
        continue

    if numero < respuesta:
        print("El número secreto es menor")
    elif numero > respuesta:
        print("El número secreto es mayor")
    else:
        print(f"¡Felicidades! Has adivinado el número secreto: {numero}")
        print("Fin del juego")
        confirmador = True


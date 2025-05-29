'''
Clase:        Fundamentos de programación
Tema:         Bucles for y while
Ejercicio:    5.3.1. Suma de valores
Descripción:  Devuelve la suma de todos los items dentro de una lista.

Autor:        Elías Josué Ventura Villatoro
Fecha:        2025-05-29
Estado:       [ Terminado ]
'''

def sumar(lista):
    aux = 0
    for item in lista:
        print(aux)
        aux = aux + item
    return aux
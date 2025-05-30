'''
Clase:        Fundamentos de programación
Tema:         Clase 9
Ejercicio:    6.2.1 Eliminando valores duplicados
Descripción:  Dada una lista de números ingresada por el usuario, retorna una lista sin números duplicados.

Autor:        Elías Josué Ventura Villatoro
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''

valores = input("¿Cuáles son sus números? ")

valores = valores.split()

aux = ""

for numero in valores:
    if numero not in aux:
        aux = aux + numero + " "

print(aux)
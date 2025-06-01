'''
Clase:        Fundamentos de programación
Tema:         Clase 9
Ejercicio:    6.3.1 Números líderes
Descripción:  Dada una lista de números ingresada por el usuario, retorna una lista de números que sean mayores a todos los de su derecha.

Autor:        Elías Josué Ventura Villatoro
Fecha:        2025-05-31
Estado:       [ Terminado ]
'''

entrada = input("¿Cuál es su lista de números? ")
entrada = entrada.split()

lista = []
aux = []

for i in entrada:
    i = int(i)
    lista.append(i)
    aux.append(i)

final = []

for numero in lista[:-1]:
    aux.remove(numero)
    for prueba in aux:
        if numero <= prueba:
            break
    else:
        final.append(numero)

print(*final)
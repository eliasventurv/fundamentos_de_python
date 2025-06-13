'''
Clase:        Fundamentos de programación
Tema:         Manejo de matrices
Ejercicio:    10.3.1. Matriz simétrica
Descripción:  Descubre si una matriz es simétrica en relación a su diagonal principal.2

Autor:        Elías Josué Ventura Villatoro
Fecha:        2025-06-13
Estado:       [ Terminado ]
'''

m_size = input("¿Cúal es el tamaño de su matriz? ")
m_size = int(m_size)
matriz = []

# Crea la matriz en el formato correcto.
for i in range(m_size):
    raw = input(f"Introduzca los datos de la fila {i}: ")
    cooked = raw.split(",")
    prelist = []

    for i in cooked:
        a = int(i)
        prelist.append(a)
        
    matriz.append(prelist)

# Revisa si una matriz es simétrica o no según su diagonal principal.
confirmador = True

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] != matriz[j][i]:
            confirmador = False

if confirmador == True:
    print("La matriz es simétrica.")
else:
    print("La matriz no es simétrica.")
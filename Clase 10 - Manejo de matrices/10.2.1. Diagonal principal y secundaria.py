'''
Clase:        Fundamentos de programación
Tema:         Manejo de matrices
Ejercicio:    10.2.1. Diagonal principal y secundaria
Descripción:  Devuelve dos listas, una con los items de la diagonal principal y otra con los de la diagonal secundaria.

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


diag_prin = []
diag_sec = []
for filas in matriz:
    for caracter in filas:
        # Crea la lista de items en la diagonal principal.
        if matriz.index(filas) == filas.index(caracter):
            diag_prin.append(caracter)
        # Crea la lista de items en la diagonal secundaria.
        if matriz.index(filas) + filas.index(caracter) == (m_size-1):
            diag_sec.append(caracter)

print(diag_prin)
print(diag_sec)
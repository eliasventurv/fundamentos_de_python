'''
Clase:        Fundamentos de programación
Tema:         Manejo de matrices
Ejercicio:    10.3.2. Juego del entorno
Descripción:  Cuenta la cantidad de números "1" que hay alrededor de un item dentro de una matriz.

Autor:        Elías Josué Ventura Villatoro
Fecha:        2025-06-13
Estado:       [ Terminado ]
'''

# Analiza la cantidad de "1" que hay alrededor de un determinado item en una matriz.
def surroundings(matrix, fila, columna):
    
    size_h = len(matrix)
    size_v = len(matrix[0])

    vertical = [fila-1, fila, fila+1]
    horizontal = [columna-1, columna, columna+1]

    count = 0

    for i in vertical:
        for j in horizontal:
            if i < 0 or j < 0:
                pass
            elif i > size_h-1 or j > size_v-1:
                pass
            elif fila == i and columna == j:
                pass
            elif matriz[i][j] == 1:
                count = count+1

    return count

m_vsize = input("¿Cúal es el tamaño vertical de su matriz? ")
m_hsize = input("¿Cuál es el tamaño horizontal de su matriz? ")
m_vsize = int(m_vsize)
m_hsize = int(m_hsize)
matriz = []

# Crea la matriz en el formato correcto.
for i in range(m_vsize):
    raw = input(f"Introduzca los datos de la fila {i}: ")
    cooked = raw.split(",")
    prelist = []

    for i in cooked:
        a = int(i)
        prelist.append(a)
        
    matriz.append(prelist)

# Analiza a cada uno de los items de la matriz.
todo = []
for i in range(m_vsize):
    pretodo = []
    for j in range(m_hsize):
        pretodo.append(surroundings(matriz, i,j))

    todo.append(pretodo)

for i in todo:
    print(i)

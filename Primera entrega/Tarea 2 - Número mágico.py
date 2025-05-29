'''
Clase:        Fundamentos de programación
Tema:         Bloque condicional
Ejercicio:    El número mágico
Descripción:  Encuentra si un número es divisible entre 7 pero no entre 5.

Autor:        Elías Josué Ventura Villatoro
Fecha:        2025-05-15
Estado:       [ Terminado ]
'''

def magico(numero):

    if (numero % 7 == 0) and (numero % 5 != 0):
        return True
    
    else:
        return False
    
print(magico(28))
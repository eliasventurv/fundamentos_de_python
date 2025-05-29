'''
Clase:        Fundamentos de programación
Tema:         Variables, tipos, entradas y salidas
Ejercicio:    Generador del correo de Key
Descripción:  Genera un correo con el dominio de Key tomando un nombre completo.

Autor:        Elías Josué Ventura Villatoro
Fecha:        2025-05-15
Estado:       [ Terminado ]
'''

def usuario(nombre):

    nombre = nombre.lower()
    palabras = nombre.split()
    
    usuario = palabras[0] + "." + palabras[2] + "@keyinstitute.edu.sv"
    
    return usuario

print(usuario("Elías Josué Ventura Villatoro"))

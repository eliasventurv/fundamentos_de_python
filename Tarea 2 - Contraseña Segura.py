'''
Clase:        Fundamentos de programación
Tema:         Bloque condicional
Ejercicio:    Contraseña segura
Descripción:  Genera un correo con el dominio de Key tomando un nombre completo.

Autor:        Elías Josué Ventura Villatoro
Fecha:        2025-05-15
Estado:       [ Terminado ]
'''

def contra(clave):

    longitud = False
    mayuscula = False
    numero = False

    if len(clave) >= 8:
        longitud = True

    for i in clave:
        if i.isupper() == True:
            mayuscula = True
            break

    for i in clave:
        if i.isdigit() == True:
            numero = True
            break

    if longitud and mayuscula and numero == True:
        print("Contraseña segura")

    else:
        print("Contraseña insegura")

contra("Eliasjos9")
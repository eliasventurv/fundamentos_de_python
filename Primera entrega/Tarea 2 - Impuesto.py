'''
Clase:        Fundamentos de programación
Tema:         Bloque condicional
Ejercicio:    Cálculo de impuesto
Descripción:  Cálcula el impuesto según cantidad de unidades.

Autor:        Elías Josué Ventura Villatoro
Fecha:        2025-05-15
Estado:       [ Terminado ]
'''

def impuesto(unidades):

    if unidades <= 100:
        return 0
    
    elif unidades <= 200:
        impuesto = unidades*0.5
        return impuesto

    else:
        impuesto = unidades*0.7
        return impuesto
    
print(impuesto(201))
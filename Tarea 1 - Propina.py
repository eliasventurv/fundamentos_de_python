'''
Clase:        Fundamentos de programación
Tema:         Variables, tipos, entradas y salidas
Ejercicio:    Automatizando el cálculo de la propina
Descripción:  Cálculo de una propina con el total de una cuenta y un porcentaje.

Autor:        Elías Josué Ventura Villatoro
Fecha:        2025-05-15
Estado:       [ Terminado ]
'''

def propina(costo, porcentaje):

    porcentaje = porcentaje/100
    propina = costo*porcentaje

    print(f"Total de la cuenta: {costo}\nPropina: {propina}\nTotal: {costo+propina}")

propina(100, 10)
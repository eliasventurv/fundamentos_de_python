'''
Clase:        Fundamentos de programación
Tema:         Bucles for y while
Ejercicio:    5.4.2. Sumador de valores posicionales
Descripción:  Suma las cifras de un número hasta obtener un número de una única cifra.

Autor:        Elías Josué Ventura Villatoro
Fecha:        2025-05-29
Estado:       [ Terminado ]
'''

numero = input("Ingresa un número: ")

print(f"\nProceso de reducción para {numero}:")

while len(numero) != 1:
    
    aux = 0

    for cifra in numero:
        cifra = int(cifra)
        aux = aux + cifra

    print(f"{numero} = {aux}")

    numero = str(aux)

else:
    print("")

print(f"El resultado final es: {numero}")


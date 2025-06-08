'''
Clase:        Fundamentos de programación
Tema:         Introducción a NumPy
Ejercicio:    5. Cuestionario de trabajo
Descripción:  Resolución de Guía de introducción a NumPy

Autor:        Elías Josué Ventura Villatoro
Fecha:        2025-06-1
Estado:       [ Terminado ]
'''


import numpy as np

# Definición de la matriz consumo
consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])

# Exploración inicial de los datos
print("Dimensiones:", consumo.ndim)
print("Forma:", consumo.shape)
print("Tipo de datos:", consumo.dtype)
print("Consumo primer hogar:", consumo[0])
print("Consumo el miércoles (día 3):", consumo[:, 2])

# Promedio de consumo por hogar
promedio_por_hogar = np.mean(consumo, axis=1)

# Promedio de consumo diario de todos los hogares
promedio_por_dia = np.mean(consumo, axis=0)

# Suma total de consumo en la semana de los 10 hogares
total_consumo = np.sum(consumo)

print(promedio_por_hogar)
print(promedio_por_dia)
print(total_consumo)

# Máximo por hogar
maximos = np.max(consumo, axis=1)

# Mínimo por día
minimos = np.min(consumo, axis=1)

# Desviación estándar global
desviacion = np.std(consumo)

print(maximos)
print(minimos)
print(desviacion)

# Suma por hogar (semana)
consumo_total_hogar = np.sum(consumo, axis=1)
# Índice del hogar con mayor consumo
hogar_mayor_consumo = np.argmax(consumo_total_hogar)
# Índice del hogar con mejor consumo
hogar_mas_eficiente = np.argmin(consumo_total_hogar)

print(consumo_total_hogar)
print(hogar_mayor_consumo)
print(hogar_mas_eficiente)


# Imprime la variable de consumo total por cada hogar
print(f"Consumo total de cada hogar durante la semana: {consumo_total_hogar}")

# Compara cada hogar conun valor mayor a 100
altos = consumo_total_hogar > 100

# Filtrando hogares que cumplen la condición:
consumo_mayor_100 = np.where(altos)[0]

print(f"ids de hogares con consumo mayor a 100: {consumo_mayor_100}")

# Aplicando normalización MinMax al conjunto de datos
consumo_normalizado = (consumo - consumo.min()) / (consumo.max() - consumo.min())

# Resultado
print(consumo_normalizado)


#RESPUESTAS DE CUESTIONARIO

# 1. ¿Cuál es el consumo del hogar 5 el viernes (día 5)? 
# R// El consumo del hogar 5 en el día 5 fue de 17.4 kWh
print("El consumo del hogar 5 en el día 5 fue de: ", consumo[4,4], "kWh")

# 2. Usando indexación, muestra el consumo de los últimos 3 hogares el domingo.
# R// El consumo de los últimos 3 hogares el domingo fue de 12, 16.7 y 9.3 respectivamente.
print(consumo[7:, 6])

# 3. Calcula el promedio de consumo los fines de semana (sábado y domingo, columnas 5 y 6).
# R// El promedio de consumo de los fines de semana fue: 13.75 kWh
print("El promedio de consumo de los fines de semana fue:", np.mean(consumo[:, 5:6]), "kWh")

# 4. ¿Qué día de la semana tiene la mayor desviación estándar entre hogares? Explica qué indica esto.
# R// El día con mayor desviación es el día 5 (sábado). Esto significa que los datos del consumo de este día están más dispersos en relación a la media.

desviaciones = []
for column in range(consumo.shape[1]):
    desviacion = np.std(consumo[:, column])
    desviaciones.append(desviacion)

print(f"La mayor desviación estándar fue: {max(desviaciones)} y pertenece al día {desviaciones.index(max(desviaciones))}")

# 5. Identifica los 3 hogares con menor consumo total durante la semana. Muestra sus índices y valores.
# Los hogares con menor consumo total fueron 9 (con 62.6), 3 (con 66.1) y 1 (77.1).

totales = np.sum(consumo, axis=1)
hogares = []
hog_ind = []

for i in range(3):
    hogar = min(totales)
    index = np.argmin(totales)
    hogares.append(hogar)
    hog_ind.append(index)
    totales = np.delete(totales, index) # Uso de IA, para descubrir función delete.

print(f"Los 3 hogares con menor consumo utilizaron: ", end="") 
print(*hogares, end="") 
print(f" y sus índices fueron: ", end="")
print(*hog_ind, end="")
print(" respectivamente")

# 6. Si el hogar 3 aumenta su consumo en un 10% cada día, ¿cuál sería su nuevo consumo total semanal?

# Dado que cada día aumentará 10% en comparación al día original, puede obtenerse factor común:
# 1.1(día1)+1.1(día2)+1.1(día3)+ ... = 1.1(día1 + día2 + día3 + ...)
# Por lo tanto, el 110% del consumo total será la suma del 110% de cada día. Así:

total3 = totales[2]
total3_aumento = total3*1.1

print("El nuevo total del hogar 3, después de aumentarlo en 10%, será: ", total3_aumento)
"""
Ejercicio 93
Filtrar numeros negativos de una lista
utilizando filter
"""

numeros = [-3, 1, -5, 5, -45]

negativos = list(filter(lambda x:x<0, numeros))

print(numeros)
print(negativos)
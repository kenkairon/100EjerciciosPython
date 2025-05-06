"""
Ejercicio 94
Filtrar cadenas que contienen
un carácter específico
usando filter
"""

cadenas = ['apple', 'python', 'Hola']
caracter = 'a'

busqueda_a = list(filter(lambda x: caracter in x, cadenas))

print(cadenas)
print(busqueda_a)
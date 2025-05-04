"""
Ejercicio 81
Elevar al cuadrado una lista de números
utilizando map
"""

def cuadrado(numeros):
    return numeros ** 2

numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(cuadrado, numeros))
print("Lista original:", numeros)
print("Lista de cuadrados:", cuadrados)
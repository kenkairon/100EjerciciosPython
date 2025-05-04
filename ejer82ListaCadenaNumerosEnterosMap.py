"""
Ejercicio 82
converir una lista de cadenas que
sean números a enteros utilizando map
"""

def converir_a_entero(cadena):
    return int(cadena)

cadenas = ["1", "2", "3", "4", "5"]
enteros = list(map(converir_a_entero, cadenas))
print("Lista original:", cadenas)
print("Lista de enteros:", enteros)
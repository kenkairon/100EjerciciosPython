"""
Ejercicio 96
Crear una excepción que me ayude 
a determinar si el índice de una
lista esta fuera de rango
"""

mi_lista = [1,2,3]

try:
    print(mi_lista[5])
except IndexError:
    print("Error el índice No Existe")
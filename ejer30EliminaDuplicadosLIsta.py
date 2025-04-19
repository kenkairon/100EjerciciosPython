"""
Ejercicio 30
ELimina duplicados de una lista
"""

lista = [1, 2, 2, 3, 4, 4, 5]    # Lista con duplicados 
sin_duplicados = list(set(lista))  # Elimina duplicados convirtiendo a conjunto y luego de nuevo a lista
print(sin_duplicados)  # Imprime la lista sin duplicados
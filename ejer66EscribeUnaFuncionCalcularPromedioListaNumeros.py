"""
Ejercicio 66
Escribe una función para calcular
el promedio de una lista de números.
"""

def promedio(lista):
    return sum(lista) / len(lista) 

resultado = promedio([4, 6, 8, 10])
print(f"El promedio de la lista es: {resultado}")
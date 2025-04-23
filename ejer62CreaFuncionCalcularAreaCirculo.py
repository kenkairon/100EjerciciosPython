"""
Ejercicio 62 
Crea una función para calcular
el área de un círculo.
"""

import math

def area_circulo(radio):
    return math.pi * radio ** 2

resultado = area_circulo(5) # Cambia el valor de radio para probar con otros valores
print(f"El área del círculo con radio 5 es: {resultado:.2f}")
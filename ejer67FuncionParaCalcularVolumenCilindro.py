"""
Ejercicio 67 
Escribe una función para calcular
el volumen de un cilindro.
V = pi * r^2 * h
"""

import math
def volumen_cilindro(radio, altura):
    return math.pi * (radio ** 2) * altura

resultado = volumen_cilindro(3, 5)
print(f"El volumen del cilindro es: {resultado:.2f} unidades cúbicas")
    
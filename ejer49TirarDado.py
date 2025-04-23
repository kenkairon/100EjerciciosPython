"""
Ejercicio 49
Simular un lanzamiento
de dado hasta obtener 6
"""

import random 
numero = 0
while numero != 6:
    numero = random.randint(1, 6)
    print(f"Has sacado un {numero}")
print("Has sacado un 6, fin del juego")
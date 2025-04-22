"""
Ejercicio 44
Genera un número aleatorio entre 1 y 10
Luego, pide al usuario que adivine el número
hasta que lo haga correctamente
"""

import random
numero_secreto = random.randint(1, 10)

intentos = 0

while True:
    intento = int(input("Adivina el número entre 1 y 10: "))
    intentos = intentos + 1
    if intentos == numero_secreto:
        print("¡Felicidades! Adivinaste el número en", intentos, "intentos.")
        break
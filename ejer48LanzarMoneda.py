"""
Ejercicio 48
Simular un volado 
lanzaminento de una moneda
"""
import random

while True:
    moneda = random.randint(0, 1)
    if moneda == 1:
        print("Cayo cara")
    else:
        print("Cayo cruz")
    jugar = input("¿Desea jugar nuevamente? (s/n): ")
    if jugar.lower() == 'n':
        break
print("Gracias por jugar")
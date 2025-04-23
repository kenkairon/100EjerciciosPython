"""
Ejercicio 59
Pedir al Usuario un Número
e imprimir la tabla de multiplicar de ese número.
"""

numero = int(input("Ingrese un número: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")      
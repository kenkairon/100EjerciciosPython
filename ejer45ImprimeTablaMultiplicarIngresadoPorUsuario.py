"""
Ejercicio 45
Imprime la tabla de multiplicar de
un número ingresado por el usuario
"""

numero = int(input("Ingrese un número: "))
i = 1
while i <= 10:
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    i += 1


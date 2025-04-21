"""
Ejercicio 38
Determina si un número es
divisible entre 5 y 7   
"""

numero = int(input("Ingrese un número: "))

if numero % 5 == 0 and numero % 7 == 0:
    print(f"{numero} es divisible entre 5 y 7")
else:
    print(f"{numero} no es divisible entre 5 y 7")
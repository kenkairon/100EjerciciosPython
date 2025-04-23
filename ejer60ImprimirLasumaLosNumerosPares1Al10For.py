"""
Ejercicio 60
Imprimir la suma de los
números pares del 1 al 10 utilizando un bucle for.
"""

suma_pares = 0
for i in range(1, 11):
    if i % 2 == 0:
        suma_pares = suma_pares + i
print("La suma de los números pares del 1 al 10 es:", suma_pares)
"""
Ejercicio 33
Determina si un año es bisiesto o no.
Regla del negocio
    Divisible por 4
    NO divisible por 100
    Divisible por 400
"""

anio = 2025

if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
    print(f"{anio} es un año bisiesto")
else:
    print(f"{anio} no es un año bisiesto")
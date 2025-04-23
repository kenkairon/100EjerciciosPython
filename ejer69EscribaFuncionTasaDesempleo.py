"""
Ejercicio 69
Escribe una función para calcular
la tasa de desempleo
td = (número de desempleados / población activa) * 100
"""

def tasa_desempleo(no_em, si_em):
    return (no_em) / si_em * 100

resultado = tasa_desempleo(100, 900)
print(f"La tasa de desempleo es: {resultado:.2f}%")
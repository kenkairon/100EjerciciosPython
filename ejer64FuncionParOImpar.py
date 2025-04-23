"""
Ejercicio 64
Escribe una función para verificar
si un número es par o impar.
"""

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
resultado = es_par(10)
print(f"El número es {'par' if resultado else 'impar'}")
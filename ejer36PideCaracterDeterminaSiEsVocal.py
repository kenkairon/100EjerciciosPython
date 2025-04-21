"""
Ejercicio 36
Pide un  caracter y Determina 
si es vocal.
"""

caracter = input("Ingrese un caracter: ")
vocales = ['a', 'e', 'i', 'o', 'u']

if caracter.lower() in vocales:
    print("Es una vocal")
else:
    print("No es una vocal")

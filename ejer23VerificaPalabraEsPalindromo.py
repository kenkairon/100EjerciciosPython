"""
Ejercicio 23
Verifica si una 
palabra es un palíndromo
"""

palabra = 'radar'

es_palindromo = palabra == palabra[::-1] # Verifica si la palabra es igual a su reverso
print(f"La palabra '{palabra}' es un palíndromo: {es_palindromo}") # Imprime el resultado de la verificación
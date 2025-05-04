"""
Ejercicio 85 
Contar el número de vocales en
una lista de palabras utilizando map
"""

def contar_vocales(palabra):
    return sum(1 for letra in palabra if letra.lower() in 'aeiou')

palabras = ['Hola', 'Mundo']

conteos = list(map(contar_vocales, palabras))
print("Lista original:", palabras)
print("Conteo de vocales:", conteos)
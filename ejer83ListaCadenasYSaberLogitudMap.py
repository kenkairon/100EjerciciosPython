"""
Ejercicio 83 
Calcular la Longitud de una lista de
palabras utilizando map
"""

def longitud(palabra):
    return len(palabra)

conjunto = ["Hola", "Mundo", "Python", "Map"]
longitudes = list(map(longitud, conjunto))
print("Lista original:", conjunto)
print("Lista de longitudes:", longitudes)
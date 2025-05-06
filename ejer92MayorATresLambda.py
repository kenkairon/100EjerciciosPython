"""
Ejercicio 92
Filtrar cadenas de longitud mayor a 3
de una lista usando filter
"""

cadenas = ["python", "ruby", "php","java"]
resultado = list(filter(lambda x:len(x) > 3, cadenas))

print(resultado)
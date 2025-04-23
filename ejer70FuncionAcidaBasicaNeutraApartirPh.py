"""
Ejercicio 70 
Escribe una función para
clasificar si una sustancia
es ácida, básica o neutra a partir de su pH.
"""

def sustancia(ph):
    if ph < 7:
        return "ácida"
    elif ph > 7:
        return "básica"
    else:
        return "neutra"
    
resultado = sustancia(7)    
print(f"El pH es {resultado}.")
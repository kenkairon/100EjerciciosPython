"""
EJercicio 27
Realiza Operaciones Básicas
con conjuntos union e intersección.
"""

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

# Unión de conjuntos
union =  conjunto1 | conjunto2  # O también: conjunto1.union(conjunto2)
interseccion = conjunto1 & conjunto2  # O también: conjunto1.intersection(conjunto2)

print("Unión:", union)  # Imprime la unión de los conjuntos
print("Intersección:", interseccion)  # Imprime la intersección de los conjuntos    
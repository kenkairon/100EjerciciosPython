"""
Ejercicio 42
Solicita al usuario ingresar un
número N y luego imprime la suma
de todos los números desde 1 hasta N
"""
# Solicitamos al usuario que ingrese un número
numero = int(input("Ingrese un número: "))
# Inicializamos la variable suma en 0
suma = 0
# Inicializamos la variable i en 1
i = 1   
# Mientras i sea menor o igual a numero
while i <= numero: 
    # Sumamos i a suma
    suma += i   
    # Incrementamos i en 1
    i += 1
print('La suma es',suma)    

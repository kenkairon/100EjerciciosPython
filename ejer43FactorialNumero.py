"""
Ejercicio 43
Solicita al usuario ingresar un
número n e imprime el factorial de
ese número EJEMPLO de 5
5! = 5 * 4 * 3 * 2 * 1 = 120
"""
# Solicitamos al usuario que ingrese un número
numero = int(input("Ingrese un número: "))
# Inicializamos la variable factorial en 1
factorial = 1
# Inicializamos la variable i en 1
i = 1
# Mientras i sea menor o igual a numero
while i <= numero:
    # Multiplicamos factorial por i
    factorial = factorial * i
    # Incrementamos i en 1
    i += 1
print('El factorial de', numero, 'es', factorial)
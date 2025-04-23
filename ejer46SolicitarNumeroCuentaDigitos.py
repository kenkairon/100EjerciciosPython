"""
Ejercicio 46
Solicita al usuario ingresar un
número y cuenta cuántos dígitos tiene
"""
numero = int(input("Ingrese un número: "))
contador = 0

while numero != 0:
    numero = numero // 10
    contador = contador + 1
    
print("Dígitos de son ", contador)
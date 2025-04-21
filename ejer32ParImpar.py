"""
Ejercicio 32
Pide un número Y Comprueba
si el número es par o impar.
"""   


numero = int(input("Introduce un número: "))
if numero % 2 == 0:
    print("El número es par.")
elif numero % 2 != 0:
    print("El número es impar.")
else:
    print("El número es cero.")
# El número es cero.
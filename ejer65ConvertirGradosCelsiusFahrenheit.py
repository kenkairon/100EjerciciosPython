"""
Ejercicio 65
Escribe  una función para convertir 
grados celsius a fahrenheit 
"""

def celsiusAFahrenheit(celsius):
    return (celsius * 9 / 5) + 32

celsius = int(input("Ingrese grados Celsius: "))
resultado = celsiusAFahrenheit(celsius)
print(f"{celsius} grados Celsius son {resultado} grados Fahrenheit")
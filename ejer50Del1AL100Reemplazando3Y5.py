"""
Ejercicio 50 
Mostrar los números del 1 al 100
pero reemplazando los múltiplos de 3 por 
"Fizz", y los múltiplos de 5 por "Buzz".
"""

numero = 1

while numero <= 100:
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)
    numero = numero + 1
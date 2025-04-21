"""
Ejercicio 40
Calcular el IMC e interpretarlo
"""

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura ** 2)
print(imc)

if imc < 18.5:
    print("Bajo peso")
elif 18.5 <= imc < 24.9:
    print("Peso normal")
elif 25 <= imc < 29.9:
    print("Sobrepeso")
elif 30 <= imc < 34.9:
    print("Obesidad grado 1 (moderada)")
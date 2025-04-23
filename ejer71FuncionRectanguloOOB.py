"""
Ejercicio 71
Crear una clase de rectangulos con los siguientes atributos
base: base del rectangulo
alto: alto del rectangulo
La clase debe tener los siguientes metodos:
** __init__(self, base, altura): Inicializa los atributos de la clase
los atributos de la clase
** calcular_area(self): Calcula y devuelve el area del rectangulo
** calcular_perimetro(self): Calcula y devuelve el perimetro del rectangulo
"""

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
rect1 = Rectangulo(5, 3)

print("Area del rectangulo:", rect1.calcular_area())
print("Perimetro del rectangulo:", rect1.calcular_perimetro())
"""
Ejercicio 72
Crear una clase Ciculo con los siguientes 
atributos
* radio : radio del circulo

La clase debe tener los siguientes metodos:
* __init__(self, radio): Inicializa los atributos de la clase

* calcular_area(self): Calcula y devuelve el area del circulo   
* calcular_perimetro(self): Calcula y devuelve el perimetro del circulo

"""
import math
class Circulo:
    def __init__(self, radio):
        self.radio = radio
        
    def calcular_area(self):
        return math.pi * (self.radio ** 2)
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
    
circulo1 = Circulo(5)

print("Area del circulo:", circulo1.calcular_area())
print("Perimetro del circulo:", circulo1.calcular_perimetro())
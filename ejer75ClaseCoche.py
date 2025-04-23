"""
Ejercicio 75
Crear una clase coche con los atributos
marca, modelo, matricula, km
con los metodos:
init como constructor
avanzar(km): este aumenta
el valor del km en la cantidad
"""

class Coche:
    def __init__(self, marca, modelo, matricula, km):
        self.marca = marca
        self.modelo = modelo
        self.matricula = matricula
        self.km = km
    
    def avanzar(self, km):
        self.km = self.km + km  
        return self.km
    
coche1 = Coche("Renault", "Clio", "1234ABC", 5000)
print(coche1.__dict__)
coche1.avanzar(3000)
print(coche1.__dict__)

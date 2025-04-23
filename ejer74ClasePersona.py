"""
Ejercicio 74 
Crear una clase Persona con los siguientes atributos:
*** nombre, edad, dni

con los metodos:
init()
es_mayor_de_edad() : devuelve True si la persona es mayor de edad, False en caso contrario
"""

class Persona:
    def __init__(self,nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False
        
persona1 = Persona("Juan", 20, "12345678A")
print("Nombre:", persona1.nombre)
if persona1.es_mayor_de_edad():
    print("Es mayor de edad")
else:
    print("No es mayor de edad")
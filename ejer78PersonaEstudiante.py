"""
Ejercicio 78
Crea una Clase persona y otra clase 
Estudiante
La clase persona tiene el atributo nombre
y el metodo mostrar_nombre()
la clase Estudiante hereda de la clase 
Persona y utilizar el metodo mostrar_nombre()
de la clase Persona
"""

class Persona:
    
    def __init__(self, nombre):
        self.nombre = nombre
        
    def mostrar_nombre(self):
        print(self.nombre)
        
class Estudiante(Persona):
    
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def mostrar(self):
        super().mostrar_nombre()
        
estudiante1 = Estudiante("Jose")
estudiante1.mostrar()  # Salida: Jose
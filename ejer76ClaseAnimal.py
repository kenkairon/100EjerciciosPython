"""
Ejercicio 76
Crear una clase animal con los atributos
especie y nombre
La clase debe tener los metodos 
init y hablar()
el metodo hablar nos retorna una palabra 
según la interpretación del sonido como perro
seria "guau"
"""
class Animal():
    
    def __init__(self, especie, nombre):
        self.especie = especie
        self.nombre = nombre
        
    def hablar(self):
        if self.especie == "perro":
            print("guau")
        elif self.especie == "gato":
            print("miau")
        else:
            print("no se que sonido hace")
            
perro = Animal("perro", "firulais")
gato = Animal("gato", "michi")

perro.hablar()  # Salida: guau
gato.hablar()  # Salida: miau     

print(perro.__dict__)  
            
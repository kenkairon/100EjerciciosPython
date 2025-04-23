"""
EJercicio 73
Crear una clase Libro
atributos:
titulo, autor, editorial, año de publicacion
Metodos
constructor para inicializar los atributos
"""

class Libro:
    def __init__(self,titulo, autor, editorial, anio_publicacion ):    
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.anio_publicacion = anio_publicacion
        

mi_libro = Libro("El Quijote", "Miguel de Cervantes", "Editorial Espasa", 1605)
print(mi_libro.__dict__)    
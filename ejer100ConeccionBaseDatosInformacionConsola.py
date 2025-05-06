"""
Ejercicio 100
Conectarte a una base de datos mysql, hacer 
una consulta a una tabla y mostrar la información 
en la consola
"""

import mysql.connector

class Conexion:
    @staticmethod
    def conectar():
        conexion = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password ='tucontraseña', # Tu contraseña de la base de datos
            database = 'visitas'
        )
        return conexion
    
class Visitas(Conexion):    
    def consulta_select(self):
        conexion = self.conectar()
        sql = "SELECT id, paterno FROM t_visitas"
        cursor = conexion.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall() 
        cursor.close()
        conexion.close()
        return registros
    
    def imprimir_datos(self):
        datos = self.consulta_select()
        for fila in datos:
            print(fila)
            
visita = Visitas()
visita.imprimir_datos() 
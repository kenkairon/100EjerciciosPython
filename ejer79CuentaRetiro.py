"""
Ejercicio 79
Representa una cuenta bancaria
con deposito y retiro
debe utilizar un titular y un saldo
Utiliza POO
"""

class Cuenta:
    
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self, cantidad):
        self.saldo +=cantidad
        print("Se deposito: ", cantidad)
        
    def retirar(self, cantidad):
        self.saldo -=cantidad
        print("Se retiro: ", cantidad)
        
    def mostrar(self):
        print(self.__dict__)
        
cuenta1 = Cuenta("Juan", 1000)
cuenta1.mostrar()  # Salida: {'titular': 'Juan', 'saldo': 1000}
cuenta1.depositar(1000)  # Salida: Se deposito:  500
cuenta1.mostrar()  # Salida: {'titular': 'Juan', 'saldo': 2000}
cuenta1.retirar(300)  # Salida: Se retiro:  500     
cuenta1.mostrar()  # Salida: {'titular': 'Juan', 'saldo': 1700}
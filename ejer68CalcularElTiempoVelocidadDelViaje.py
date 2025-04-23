"""
EJercicio 68
Escriba una función que pida por teclado
la distancia y la velocidad
para poder calcular el tiempo de viaje
"""

def tiempo_viaje():
    distancia = int(input("Ingrese la distancia en km: "))
    velocidad = int(input("Ingrese la velocidad en km/h: "))
    
    return distancia / velocidad

resultado = tiempo_viaje()
print(f"El tiempo de viaje es: {resultado} horas")
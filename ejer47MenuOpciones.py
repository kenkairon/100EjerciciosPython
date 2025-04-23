"""
Ejercicio 47
Hacer un menú de opciones que incluya la opción
de salir un programa
"""

while True:
    print("1- Sumar")
    print("2- Restar")
    print("3- Salir")
    
    opcion = int(input("Ingrese una opción: "))
    
    if opcion == 1:
        print("Usted esta sumando")
    elif opcion == 2:
        print("Usted esta restando")
    elif opcion == 3:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intente nuevamente")

print("Vuelve pronto")
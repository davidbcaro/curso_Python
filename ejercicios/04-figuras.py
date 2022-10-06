menu = """ 
Seleccione una opción
(1) Área cuadrado
(2) Área rectángulo
(3) Área circulo
"""
opcion = int(input(menu))

if opcion == 1:
    lado = int(input("Ingrese el valor del lado (cm): "))
    area_c = lado * lado
    print("El área del cuadrado es: ", area_c)
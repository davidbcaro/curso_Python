# def bienvenida(nombre):
#     mensaje = f"Bienvenido {nombre}"
#     return mensaje

# texto = bienvenida("David")
# print(texto)

# def suma(a: float, b: float):
#     resultado = a + b
#     return resultado

# resultado_suma = suma(67.8, 86.7)
# print(resultado_suma)

def area_circulo(r: float, pi=3.14):
    """
    Función que calcula el área de un circulo. Recibe 
    como parámetro de entrada el radio y el valor de pi
    que por defecto es 3.14.
    """
    resultado = pi*(r**2)
    return resultado

circulo = area_circulo(8.7)
print(circulo)

help(area_circulo)

# resultado_suma = suma(3, 3)
# print("El resultado es:", resultado_suma)




def bienvenida(mensaje):
    print(mensaje)

bienvenida("Bienvenido al curso de Python")

def multiplicacion(numero1: float, numero2: float):
    resultado = numero1 * numero2
    return resultado

mult = multiplicacion(14.8, 4.8)
print(mult) 

"""
def suma(n1, n2):
    res = n1 + n2
    return res
def resta(n1, n2):
    res = n1 - n2
    return res

#print("Hola desde la funcion print soy un parametro")
num1 = 10
num2 = 50
while True:
    print(f"Selecciona que deseas hacer con estos números {num1} y {num2}:\n\
1.-Sumar\n\
2.-Restar\n\
3.-Salir")
    opcion=input()
    if opcion == '1':
        res = suma(num1, num2)
        print(f"El resultado es:{res} tipo:{type(res)}")
    elif opcion == '2':
        res = resta(num1, num2)
        print(f"El resultado es:{res} tipo:{type(res)}")
    elif opcion == '3':
        break
    else:
        print("Elije un número de las opciones")
"""

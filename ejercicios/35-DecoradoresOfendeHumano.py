'''
Crearemos un decorador que: 
    Pida 2 números y que valide que sean mayores a 0.
    Muestre el resultado de la operación.
Crear diferentes funciones matemáticas (suma, resta, multiplicacion y division) que sean validadas por el decorador
'''
def ValidarDatos(operacionMatematica):
    #Pida 2 números y que valide que sean mayores a 0.
    def antes():
        while True:
            a=int(input("por favor ingresa un número mayor a 0:"))
            b=int(input("por favor ingresa otro número mayor a 0:"))
            if a>0 and b>0:
                return a,b
            else:
                print("Los números no son mayores que cero")

    #Muestre el resultado de la operación.
    def despues(res):
        print(f"Resultado:{res}")

    def muestraDatos(*args):
        a,b=antes()
        res=operacionMatematica(a,b)
        despues(res)
    return muestraDatos

@ValidarDatos
def suma(a=0,b=0):
    return a+b
@ValidarDatos
def resta(a=0,b=0):
    return a-b
@ValidarDatos
def mul(a=0,b=0):
    return a*b
@ValidarDatos
def div(a=0,b=0):
    return a/b
@ValidarDatos
def concatenar(a=0,b=0):
    return str(a)+""+str(b)

concatenar()
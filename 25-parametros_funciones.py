'''
#Parámetro con valor por defecto.
def parametrosDefecto(n1, n2=20):
    print(f"n1={n1} y n2={n2}")
#parametrosDefecto(10,15)
parametrosDefecto(10)

#Orden de los parámetros.
def parametrosOrden(n1,n2,n3=30):
    print(f"n1={n1},n2={n2},n3={n3}")
#parametrosOrden(10,20,40)
parametrosOrden(n3=50,n2=40,n1=5)

#Enviar una lista como parámetro.
def listaParametro(numeros):
    cont=1
    for n in numeros:
        print(f"n{cont}={n}")
        cont+=1
listaParametro([1,2.2,"Hola"])

#Enviar un diccionario como parámetro.
def parametroDiccionario(numeros):
    print(numeros)
    print(f"n1={numeros['n1']} , n2={numeros['n2']}")
parametroDiccionario({'n1':1,'n2':2})
'''
#Enviar un diccionario como parámetro.
def parametroDiccionario2(**numeros):
    print(numeros)
    print(f"n1={numeros['n1']} , n2={numeros['n2']}")
parametroDiccionario2(n1=1, n2=2)
'''
En este ejercicio le mostraremos una lista de números al humano y pediremos que ingrese un número y la cantidad de veces que ese número se repite.

Crearemos una tupla con números al azar y  se la mostraremos al humano.
Pediremos al humano que ingrese un numero de la tupla y nos diga cuantas veces se repite.
Si le atina felicitamos al humano.
En caso contrario reprendemos al humano.

'''
tupla=(1,2,4,2,5,6,7,8,15,2,3)
print(tupla)
numero=int(input("Ingresa un número de la lista:"))
if numero in tupla:
    print(f"Cuántas veces se repite el número {numero} en la lista:")
    repite=int(input())
    seRepiteEnTupla=tupla.count(numero)
    if repite==seRepiteEnTupla:
        print("Correcto")
    else:
        print(f"El número {numero} se repite {seRepiteEnTupla} en la lista")
else:
    print(f"El número {numero} no esta en la lista")
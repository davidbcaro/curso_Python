'''
Mostrar los resultados.
'''
#Crear una función que pida una cantidad indeterminada de números y guardarlos en una lista.
def pideNumero():
    lista=[]
    while True:
        n=int(input("ingresa cualquier número (0 para terminar):"))
        if n==0:
            break
        else:
            lista.append(n)
    return lista
#Crear una función que busque el mayor y menor número de una lista.
def mayorMenor(lista):
    mayor=0
    menor=999999

    for numero in lista:

        if numero>mayor:
            mayor=numero

        if numero<menor:
            menor=numero
    return mayor,menor
#lista=pideNumero()
#mayor,menor=mayorMenor(lista)
mayor,menor=mayorMenor(pideNumero())
print(f"mayor={mayor},menor={menor}")
#Crear una función que pida un número mayor a 1 al humano.
def pideNumero():
    while True:
        n=int(input("Ingresa un numero mayor a 1:"))
        if n>1:
            return n

#Crear una función que genere una lista fibonacci desde 1 hasta un número x.
def generaFibonnaci(n):
    lista=[]
    for i in range(0,n):
        if i==0 or i==1:
            lista.append(1)
        else:
            lista.append(lista[-2]+lista[-1])
    return lista
#Crear una función que muestre una lista de números.
def muestraLista(lista):
    for i in lista:
        if(i!=lista[-1]):
            print(f"{i}",end="+")
        else:
            print(f"{i}")
#pide un numero humano
n=pideNumero()
#genera una susecion fibonacci
lista=generaFibonnaci(n)
muestraLista(lista)

#muestraLista(generaFibonnaci(pideNumero()))
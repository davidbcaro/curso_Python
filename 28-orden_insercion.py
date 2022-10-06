def insertarNumero():
    lista=[]
    while True:
        n=int(input("Por favor ingresa un número (0 terminar):"))
        if n==0:
            return lista
        else:
            lista.append(n)
def ordenPorInsercion(lista):
    pos=0
    i=0
    aux=0
    for _ in lista:
        pos=i
        aux=lista[i]
        while pos>0 and lista[pos-1]>aux:
            lista[pos]=lista[pos-1]
            pos=pos-1
        lista[pos]=aux
        i=i+1
    return lista
def mostrarLista(lista):
    for numero in lista:
        print(numero)
lista=insertarNumero()
lista=ordenPorInsercion(lista)
print("Lista ordenada por inserción")
mostrarLista(lista)
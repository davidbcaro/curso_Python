def pedirDatos():
    lista = []
    while True:
        n = int(input("Ingresa el numero que quieras (0 para terminar):"))
        if n == 0:
            return lista
        else:
            lista.append(n)
    return lista

def burbuja(lista):
    cont = 0
    ordenado = False
    tamano = len(lista)
    comparaciones = tamano
    for _ in range(0,tamano):
        if ordenado == True:
            break
        for j in range(0,comparaciones-1):
            ordenado = True
            cont = cont+1
            if lista[j]>lista[j+1]:
                ordenado = False
                aux=lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
        comparaciones = comparaciones-1
    return lista,cont
def mostrarLista(lista,cont):
    tam = len(lista)
    print(f"Lista ordenada en {cont} ciclos de forma acendente:")
    for i in range(0,tam):
        print(f"{lista[i]}")
    print(f"Lista ordenada en {cont} ciclos de forma desendente:")
    for i in range(tam,0,-1):
        print(f"{lista[i-1]}")

lista = pedirDatos()
lista, cont = burbuja(lista)
mostrarLista(lista, cont)
import modulos.humano as humus
import modulos.busquedas as busquedas
lista=[1,2,3,4,5,6,7,8,9,10]
while True:
    num=humus.pedirNumero(lista)
    encontrado=busquedas.busquedaBinaria(lista,num)
    if encontrado==True:
        print("Felicidades el número ingresado esta en la lista")
        break
    else:
        print("El número no esta en la lista intentalo de nuevo:")

import modulos.humano as humus
import modulos.busquedas as busquedas
lista=[1,2,3,4,5]
while True:
    num=humus.pedirNumero(lista)
    encontrado=busquedas.busquedaSecuencia(lista,num)
    if encontrado==True:
        print("Felicidades has colocado ún numero de la lista")
        break
    else:
        print("Inténtalo de nuevo:")
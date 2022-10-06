def busquedaBinaria(lista,num):
    tam=len(lista)
    cont=0
    inf=0
    sup=tam
    while inf<=sup and cont<tam:
        mitad=int((inf+sup)/2)
        if lista[mitad]==num:
            return True
        elif lista[mitad]>num:
            sup=mitad
            mitad=int((inf+sup)/2)
        elif lista[mitad]<num:
            inf=mitad
            mitad=int((inf+sup)/2)
        cont=cont+1
    return False
def busquedaSecuencia(lista,num):
    for i in range(0,len(lista)):
        if num==lista[i]:
            return True
    return False

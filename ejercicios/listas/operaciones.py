def combina(lista1,lista2):
    listaNueva=[]
    tam1=len(lista1)
    tam2=len(lista2)
    if tam1>=tam2:
        tamMayor=tam1
    else:
        tamMayor=tam2
    for i in range(0,tamMayor):
        if i<tam1:
            listaNueva.append(lista1[i])
        if i<tam2:
            listaNueva.append(lista2[i])
    return listaNueva
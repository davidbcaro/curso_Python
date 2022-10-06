def palindromo(texto):
    texto=texto.replace(" ","")
    tam=len(texto)
    cont=0
    for i in reversed(range(0,tam)):
        if texto[i].lower()!=texto[cont].lower():
            return False
        cont=cont+1
    return True
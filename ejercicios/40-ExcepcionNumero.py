def leerNumero():
    while True:
        valor=input("Ingresa un número que sea un número:")
        try:
            numero=int(valor)
            return numero
        except ValueError as ex:
            print(f"El valor '{valor}' no es número intentalo de nuevo ",ex)
lista=[]
print("Ingresa una lista de números (0 para terminar)")
while True:
    numero=leerNumero()
    if numero==0:
        break
    else:
        lista.append(numero)

print("Ingresa un índice de tu lista: ",lista)
try:
    print(f"Este es el número de tu índice ",lista[leerNumero()])
except IndexError as ex:
    print("El índice no esta en la lista ",ex)

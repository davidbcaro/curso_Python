'''
Programa que pida numero enteros y los vaya sumando.
Si el número introducido esta dentro de 100 y 200 o es 0 cerrar el programa.
'''
suma=0
while True:
    numero=int(input("Ingresa un numero entre 100 y 200 para ser sumado si presionas 0 se cierra el programa:"))
    if numero>=100 and numero<=200:
        suma=suma+numero
        print(f"El resultado es: {suma}")
    else:
        print(f"Solo se pueden sumar números entre 100 y 200 aqui esta tu suma {suma}")
    if numero==0:
        break
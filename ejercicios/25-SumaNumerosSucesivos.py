while True:
    n=int(input("Ingresa un numero mayor a 1:"))
    if n>1:
        break
    else:
        print("Te pedí un numero mayor a 1")
suma=0
strResultado=""
for i in range(1,n+1):
    suma=suma+i
    #print(f"{i}",end="+")
    strResultado=strResultado+str(i)+"+"
strResultado=strResultado[:-1]
strResultado=strResultado+"="
print(strResultado)
print(f"Resultado de la suma:{suma}")
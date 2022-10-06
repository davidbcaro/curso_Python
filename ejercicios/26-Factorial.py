while True:
    n=int(input("Ingresa un número mayor a 1:"))
    if n>1:
        break
    else:
        print("Te pedí que ingresara un número mayor a 1 intentalo de nuevo")
factorial=1
strResultado=""
for i in range(1,n+1):
    factorial=factorial*i
    strResultado=strResultado+str(i)+"*"
strResultado=strResultado[:-1]
strResultado=strResultado+"="
print(strResultado)
print(f"Factorial:{factorial}")
while True:
    n=int(input("Por favor ingresa un número mayor a 1:"))
    if n>1:
        break
    else:
        print("Te pedí un número mayor a 1")
suma=0
for i in range(1,n+1):
    potencia=pow(2,i)
    suma=suma+potencia
    if i<n:
        print(f"2^{i}({potencia})",end=" + ")
    elif i==n:
        print(f"2^{i}({potencia})",end=" = ")
print(suma)
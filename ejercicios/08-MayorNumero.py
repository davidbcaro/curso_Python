print("Ingresa dos números:")
n1=int(input("Número 1:"))
n2=int(input("Número 2:"))
if n1==n2:
    print("Los 2 números son iguales")
elif n1>n2:
    print(f"El número {n1} es mayor que {n2}")
else:
    print(f"El número {n2} es mayor que {n1}")
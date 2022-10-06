numero1=int(input("Ingresa un número par:"))
numero2=int(input("Ingresa otro número par:"))
numeroPar1=numero1%2
numeroPar2=numero2%2
if numeroPar1==0 and numeroPar2==0:
    print("Correcto, los número son pares")
else:
    if numeroPar1!=0:
        print(f"El número {numero1} no es par")
    if numeroPar2!=0:
        print(f"El número {numero2} no es par")
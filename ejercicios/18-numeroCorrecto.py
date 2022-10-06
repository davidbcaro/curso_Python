divisor = float(input("Ingresa el divisor:"))
dividendo = float(input("Ingresa un dividendo superior a 0:"))
while dividendo<=0:
    print(f"El dividendo {dividendo} debe ser superior a 0 intentalo de nuevo:")
    dividendo=float(input())

division = divisor/dividendo
print(f"El resultado de la división es:{division}")
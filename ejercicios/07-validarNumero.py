x = float(input("Ingresa el valor de x:"))
y = float(input("Ingresa el valor de y:"))
dividendo = (y**2)-1 
if dividendo != 0:
    res= ( x**(1/2) )  / dividendo
    print(f"El resultado es:{res}")
else:
    print(f"El valor de 'Y' no puede ser {y}")
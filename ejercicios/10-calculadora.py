'''
S o s: Suma.
R o r: Resta.
M o m: Multiplicación.
D o d: División.
'''
print("Ingresa dos numeros")
num1=int(input("Numero 1:"))
num2=int(input("Numero 2:"))
opcion=input("Selecciona lo que quieres hacer con estos dos números\n\
S s=Suma\n\
R r=Resta\n\
M m=Multiplicacion\n\
D d=Divicion\n"
)
opcion=opcion.lower()
res=0
if opcion=="s":
    res=num1+num2
if opcion=="r":
    res=num1-num2
if opcion=="m":
    res=num1*num2
if opcion=="d":
    if num2!=0:
        res=num1/num2
else:
    print("Elige una opción correcta")
    quit()
print(f"El resultado es:{res}")
    

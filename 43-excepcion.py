lista=[]
a=int(input("Ingresa un numero:"))
lista.append(a)
b=int(input("Ingresa un numero mayor a 0:"))
lista.append(b)

try:
    res=a/b
    print(lista[1])
except Exception as ex:
    print(ex)
finally:
    print("Fin del programa")

'''
try:
    print(lista[2])
except IndexError as ex:
    print(ex," El index 2 no existe en la lista")
'''

'''
try:
    res=a/b
except ZeroDivisionError as ex:
    print(ex)
    print("b debe ser mayor a 0")
'''

'''
if b>0:
    res=a/b
else:
    print("b debe ser mayor a 0")
'''

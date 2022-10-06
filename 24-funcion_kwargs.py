def suma(**kwargs):
    suma = 0
    for key, value in kwargs.items():
        print(key, value)
        suma += value
    return suma

resultado = suma(a=5, b=20, c=23, d=50, e=100)
print("El resultado es:", resultado)
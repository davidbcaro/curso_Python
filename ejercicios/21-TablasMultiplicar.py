while True:
    numero=int(input("Ingresa un número entre el 1 y el 10:"))
    if numero<1 or numero>10:
        print(f"El número {numero} esta fuera del rango de 1 y 10:")
    else:
        break
for i in range(10):
    print(f"{(i+1)} * {numero} = {(i+1)*numero} ")
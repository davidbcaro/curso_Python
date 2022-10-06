import random
contador=1
aleatorio=int(random.random()*100)
while True:
    numero=int(input(f"Qué número entre 1 y 100 crees que estoy pensando ({aleatorio}):"))
    if numero<aleatorio:
        print(f"El número {numero} es menor al que estoy pensando")
    elif numero>aleatorio:
        print(f"El número {numero} es mayor al que estoy pensando")
    if numero==aleatorio:
        print(f"FELICIDADES ADIVINASTE EL NÚMERO EN {contador} INTENTOS")
        break
    contador=contador+1
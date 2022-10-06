numeros = [1, 2, 34, 35]
for numero in numeros[:2]:
    print("Las numeros son:", numero)

#for numero in range(10, 0, -1):          # range(inicio, final)
#    print("Número: ", numero)

 
#for n in range(1, 6):
#    c = n**2
#    print("Número: ", n, "Cuadrado del número: ", c)


for i in range(5):
 print("Numero:", i)

for i in [5,6,7]:
    print("Numero:", i)

for i in (5,6,7):
    print("Numero:", i)

diccionario = {"Python":1, "Java":2, "JavaScript":3}
for lenguaje in diccionario:
    print(f"{lenguaje} -> {diccionario[lenguaje]} ")

for clave,valor in {"Python":1, "Java":2, "JavaScript":3}.items():
    print(f"{clave} -> {valor}")

texto = "programador"
for letra in texto:
    print("Dame una:", letra)
print("Como dice:", texto)

# Ejercicio 19 al 28
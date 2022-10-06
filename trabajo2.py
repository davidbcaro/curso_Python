
# Contar líneas del archivo 
f = open("archivo.txt", "r")
cont_lineas = 0

for linea in f:
    cont_lineas = cont_lineas + 1

print("Total de líneas:", cont_lineas)


# Contar palabras y caracteres del archivo
g = open("archivo.txt", "r")
texto = g.read()
palabras = texto.split()
cont_palabras = len(palabras)
cont_caracteres = len(texto)
print("Total de palabras:", cont_palabras)
print("Total de caracteres:", cont_caracteres)


# Contar veces que aparece una palabra en al archivo 
h = open("archivo.txt", "r")
texto = h.read()
texto = texto.lower()
palabras = texto.split()
diccionario_frecuencias = {}

for palabra in palabras:
    if palabra in diccionario_frecuencias:
        diccionario_frecuencias[palabra] += 1
    else:
        diccionario_frecuencias[palabra] = 1



# Escritura del archivo de salida
salida = open("salida.txt", mode="w", encoding="utf-8")
salida.write("Total de líneas: " + str(cont_lineas) +  "\n")
salida.write("Total de palabras: " + str(cont_palabras) + "\n")
salida.write("Total de caracteres: " + str(cont_caracteres) + "\n")
for palabra in diccionario_frecuencias:
    frecuencia = diccionario_frecuencias[palabra]
    print(f"La palabra '{palabra}' tiene una frecuencia de: {frecuencia}")
    salida.write(f"La palabra '{palabra}' tiene una frecuencia de: {frecuencia}\n")
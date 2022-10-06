'''
Trabajo individual
Presentador por: David Bohorquez
'''

# Función para contar líneas del archivo 
def contar_lineas():
    f = open("archivo.txt", "r", encoding="utf-8")
    cont_lineas = 0
    for linea in f:
        cont_lineas = cont_lineas + 1
    print("Total de líneas:", cont_lineas)
    return str(cont_lineas)


# Función para contar palabras del archivo
def contar_palabras():
    g = open("archivo.txt", "r", encoding="utf-8")
    texto = g.read()
    palabras = texto.split()
    cont_palabras = len(palabras)
    print("Total de palabras:", cont_palabras)
    return str(cont_palabras)


# Función para contar cacrcteres del archivo
def contar_caracteres():
    h = open("archivo.txt", "r", encoding="utf-8")
    texto = h.read()
    palabras = texto.split()
    cont_caracteres = len(texto)
    print("Total de caracteres:", cont_caracteres)
    return str(cont_caracteres)


# Función para contar las veces que aparece una palabra en al archivo 
def frecuencia_palabras():
    i = open("archivo.txt", "r", encoding="utf-8")
    texto = i.read()
    texto = texto.lower()
    # Remover caracteres especiales y números
    borrar = "-*?¿,;:.¡!\"'0123456789"
    for caracter in borrar:
        texto = texto.replace(caracter,"")
    palabras = texto.split()
    diccionario = {}
    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] = diccionario[palabra] + 1
        else:
            diccionario[palabra] = 1
    return diccionario


# Escritura del archivo de salida
salida = open("salida.txt", "w", encoding="utf-8")
salida.write("Total de líneas: " + contar_lineas() +  "\n")
salida.write("Total de palabras: " + contar_palabras() + "\n")
salida.write("Total de caracteres: " + contar_caracteres() + "\n")
diccionario_frecuencia = frecuencia_palabras()
for palabra in diccionario_frecuencia:
    frecuencia = diccionario_frecuencia[palabra]
    print(f"La palabra '{palabra}' tiene una frecuencia de: {frecuencia}")
    salida.write(f"La palabra '{palabra}' tiene una frecuencia de: {frecuencia}\n")
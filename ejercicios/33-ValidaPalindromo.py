import texto.reordenar as reordenar
while True:
    texto=input("Ingresa un palíndromo:")
    esPalindromo=reordenar.palindromo(texto)
    if esPalindromo==True:
        print(f"'{texto}' si es palíndromo")
        break
    else:
        print(f"'{texto}' no es palíndromo")
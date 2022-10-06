var = "Hola mundo"
dir(var)
print(var.capitalize())
print(var.upper())
print(var.lower())

# Unir cadenas
lista = ["Hola", "mundo"]
unir = "-".join(lista)
print(unir)

# Recorrrer lista e imprimir índice y valor
quesos = ['Cheddar', 'Edam', 'Gouda', 4, 5, 6]

for indice, valor in enumerate (quesos):
    print(indice, valor)
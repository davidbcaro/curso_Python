conjuntos = set()
conjuntos = {1, 2, 3, "Hola", "mundo", 1, 2, 3}
print(conjuntos)
#conjuntos.append(5)
conjuntos.add(5)
print(conjuntos)
print("3 in conjuntos=", 3 in conjuntos)
conjuntos.discard(1)
print("conjuntos.discard(1)=", conjuntos)
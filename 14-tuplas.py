tupla = (1, 2, 3, "Hola", "mundo")
#tupla.append(5)
#tupla[1] = 5
print(tupla)
print("tupla[1]=", tupla[1])
print("tupla[0:3]=", tupla[0:3])
print("3 in tupla=", 3 in tupla)
print("tupla.index(0)=", tupla.index("Hola"))
print("tupla.count(0)=", tupla.count(1))
print("len(tupla)=", len(tupla))

lista = list(tupla)
print(lista)
tupla2 = tuple(lista)
print(tupla2)
# Tuplas

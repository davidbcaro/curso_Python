'''
Crear un programa en python que tenga dos listas en las cuales eliminaremos los elementos repetidos y de los cuales obtendremos:

Elementos que aparecen en las dos listas (Unión).
Elementos que aparecen en la primer lista pero no en la segunda (Diferencia).
Elementos que aparecen en la segunda lista pero no en la primera (Diferencia).
Elementos que aparecen en Ambas listas (intersección).
'''
lista1=[1,2,2,3,4,5,4,8,45,54,87,99,5]
lista2=[1,2,4,6,2,4,5,2,45,22,55,77,88,99]
A=set(lista1)
B=set(lista2)
union=A | B
diferenciaAmenosB= A - B
diferenciaBmenosA= B - A
interseccion=A & B
print("Elementos que aparecen en las dos listas (Unión).",union)
print("Elementos que aparecen en la primer lista pero no en la segunda (Diferencia).",diferenciaAmenosB)
print("Elementos que aparecen en la segunda lista pero no en la primera (Diferencia).",diferenciaBmenosA)
print("Elementos que aparecen en Ambas listas (intersección).",interseccion)
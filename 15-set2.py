#set es una colección sin orden y sin índices, no permite elementos repetidos
#y los elementos no se pueden modificar, pero si agregar nuevos o eliminar
planetas = {
    "Marte", 
    "Júpiter", 
    "Venus"
}
print(planetas)
#longitud
print(len(planetas))
#revisar si un elemento está presente
print("Marte" in planetas)
#agregar
planetas.add("Tierra")
print(planetas)
planetas.add("Tierra")#no se pueden agregar elementos duplicados
print(planetas)
#eliminar con remove posiblemente arroja excepción
planetas.remove("Tierra")
print(planetas)
#descarta con discard no arroja excepción
planetas.discard("Júpiter")
print(planetas)
#limpiar el set
planetas.clear()
print(planetas)
#eliminar el set
del planetas
#print(planetas)


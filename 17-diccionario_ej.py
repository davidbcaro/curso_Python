#un diccionario está compuesto de llave,valor (key,value)
diccionario = {
    "IDE": "Integrated Development Environment",
    "OOP": "Object Oriented Programming",
    "DBMS": "Database Management System"
}
print(diccionario)
#longitud
print(len(diccionario))
#accediendo a un elemento
print(diccionario["OOP"])
#otra forma, mismo resultado
print(diccionario.get("OOP"))
#modificando valores
diccionario["IDE"] = "Integrated development environment"
print(diccionario)
#iterar 
for termino in diccionario:
    print(termino)

for termino in diccionario:
    print(diccionario[termino])   
     
for valor in diccionario.values():
    print(valor)

#comprobando existencia de un elemento
print("IDE" in diccionario)   

#agregar nuevos elementos
diccionario["PK"] = "Primary Key"
print (diccionario)
 
#remover elementos
diccionario.pop("DBMS")
print(diccionario) 

#limpiar 
diccionario.clear()
print(diccionario)

#eliminar por completo
#del diccionario
#print(diccionario)

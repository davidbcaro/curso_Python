archivo=open("archivos/personas.txt",encoding="utf-8")
lineas=archivo.readlines()
archivo.close()
personas=[]
for linea in lineas:
    campo=linea.replace("\n","").split(";")
    persona={"id":campo[0],"nombre":campo[1],"apellido":campo[2],"nacimiento":campo[3]}
    personas.append(persona)
for persona in personas:
    print(f"id={persona['id']} {persona['nombre']} {persona['apellido']} {persona['nacimiento']}")
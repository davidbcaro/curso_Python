'''
En este ejercicio vamos a acceder a una lista de alumnos que tengan:
nombre
edad
calificación

Además un diccionario que tenga alumnos y maestros donde:

Los alumnos tendrán:
nombre
edad
calificación

Y los maestros tendrán:
nombre
grado
'''
alumnos=[
    {"nombre":"Juan","edad":19,"calificacion":10},
    {"nombre":"Maria","edad":19,"calificacion":8},
    {"nombre":"Pedro","edad":20,"calificacion":9}
]
#for alumno in alumnos:
#    print(f"Nombre:{alumno['nombre']} Edad:{alumno['edad']} Calificacion:{alumno['calificacion']}")

escuela={
    "alumnos":alumnos,
    "maestros":[
        {"nombre":"Javier","grado":"Lic."},
        {"nombre":"Martha","grado":"Maestria"},
        {"nombre":"Pedro","grado":"Doc."},
    ]
}
print("ALUMNOS")
for alumno in escuela["alumnos"]:
    print(f"Nombre:{alumno['nombre']} Edad:{alumno['edad']} Calificacion:{alumno['calificacion']}")
print("\nMAESTROS")
for maestro in escuela["maestros"]:
    print(f"Nombre:{maestro['nombre']} Grado:{maestro['grado']}")

print(escuela)
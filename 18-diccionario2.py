alumnos={
    1:["Eugenio", "Chaparro"],
    2:["Maria", "Martinez"],
    3:["Pepe", "Fernández"]
}
'''
print(alumnos[1])
print(alumnos[2])
print(alumnos[3])
print(alumnos[4])
'''
if 1 in alumnos:
    print(alumnos[1])
else:
    print("Alumno 1 no existe")
if 2 in alumnos:
    print(alumnos[2])
else:
    print("Alumno 2 no existe")
if 3 in alumnos:
    print(alumnos[3])
else:
    print("Alumno 3 no existe")
if 4 in alumnos:
    print(alumnos[4])
else:
    print("Alumno 4 no existe")
'''
print(alumnos.get(1,"Alumno 1 no existe"))
print(alumnos.get(2,"Alumno 2 no existe"))
print(alumnos.get(3,"Alumno 3 no existe"))
print(alumnos.get(4,"Alumno 4 no existe"))
'''
print(alumnos.keys())
print(alumnos.values())
print(alumnos.items())
print(alumnos)
alumnos.clear()
print(alumnos)

# Ejercicio 13
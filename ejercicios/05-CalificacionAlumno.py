'''
Calcular las calificaciones de un alumno con las siguientes características:
Calificación de prácticas que es 40%.
Calificación de participación que es 20%.
Calificación de examen que es 40%.
Obtener la calificación final sumando y obteniendo el promedio.
'''
print("Ingresa las calificaciones del alumno:")
practicas = float(input("Calificación de las prácticas:"))
participacion = float(input("Calificación de las participaciones:"))
examen = float(input("Calificación del examen:"))
practicas *= 0.40
participacion *= 0.20
examen *= 0.40
final=practicas+participacion+examen
print(f"Esta es la calificación:{final:.2f}")
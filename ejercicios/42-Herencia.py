class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
class Maestro(Persona):
    def __init__(self,nombre,edad,grado):
        Persona.__init__(self,nombre,edad)
        self.grado=grado
class Estudiante(Persona):
    def __init__(self,nombre,edad,codigo):
        Persona.__init__(self,nombre,edad)
        self.codigo=codigo
class Universitario(Estudiante):
    def __init__(self,nombre,edad,codigo,carrera):
        Estudiante.__init__(self,nombre,edad,codigo)
        self.carrera=carrera
u1=Universitario("Eugenio",23,"02352","Sistemas")
print(u1.carrera)
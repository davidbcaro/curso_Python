class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def mostrarNombre(self):
        print("El nombre de la PERSONA es",self.nombre)
class Encargado:
    def __init__(self,codigoEncargado,departamento):
        self.codigoEncargado=codigoEncargado
        self.departamento=departamento

class EstudianteEncargado(Persona,Encargado):
    def __init__(self,nombre,edad,clave,calificacion,codigoEncargado,departamento):
        Persona.__init__(self,nombre,edad)
        Encargado.__init__(self,codigoEncargado,departamento)
        self.clave=clave
        self.calificacion=calificacion
        self.codigoEncargado=codigoEncargado
        self.departamento=departamento
    '''
    def mostrarNombre(self):
        print("El nombre del ESTUDIANTE-ENCARGADO es",self.nombre)
    '''
class Estudiante(Persona):
    def __init__(self,nombre,edad,clave,calificacion):
        Persona.__init__(self,nombre,edad)
        self.clave=clave
        self.calificacion=calificacion
estudianteEncargado1=EstudianteEncargado("Juan",22,"0232",10,"0233","Sistemas")
estudianteEncargado1.mostrarNombre()
'''
persona1=Persona("Juan",22)
persona1.mostrarNombre()
'''
#print("Nombre",estudianteEncargado1.nombre,"Departamento",estudianteEncargado1.departamento)
'''
juan=Persona("Juan",22)
print("juan.edad",juan.edad)
maria=Estudiante("Maria",23,"2222",10)
print("maria clave",maria.clave)
'''
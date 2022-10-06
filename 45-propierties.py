class Auto:
    def __init__(self,matricula):
        self.__matricula=matricula
    
    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self,valor):
        self.__matricula=valor
'''
    def getMatricula(self):
        return self.__matricula

    def setMatricula(self,valor):
        self.__matricula=valor
'''
carro1=Auto("WWW")
carro1.matricula="QQQ"
print(carro1.matricula)
'''
carro1.setMatricula("QQQ")
print(carro1.getMatricula())
'''
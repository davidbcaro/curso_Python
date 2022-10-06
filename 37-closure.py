'''
def closure(parametro):
    def funcionAretornar():
        return parametro+1
    return funcionAretornar
resibeFuncion=closure(5)
resultado=resibeFuncion()
print(resultado)
'''
def closureValidador(a,b):
    def validar():
        if a>0 and b>0:
            return True
        else:
            return False
    return validar
validado=closureValidador(0,1)
print(validado())
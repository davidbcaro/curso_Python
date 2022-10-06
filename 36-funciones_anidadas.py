def divicion(a,b):
    def validar():
        if a>0 and b>0:
            return True
        else:
            return False
    print(validar())
    if validar()==True:
        return a/b
    else:
        return None
resultado=divicion(0,0)
print(resultado)

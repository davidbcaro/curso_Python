'''
def funcionUno():
    miVariable="Hola desde funcionUno"
    miVariable=miVariablePrincipal
    miVariablefuncionUno="miVariablefuncionUno"
    print(miVariable)
def funcionDos():
    miVariable="Hola desde funcionDos"
    print(miVariable)
miVariable="Hola desde principal"
miVariablePrincipal="Estoy en principal"
miVariablefuncionUno=""
funcionUno()
funcionDos()
print(miVariablefuncionUno)
'''
def funcionUno():
    global miVariable
    miVariable="Hola desde funcionUno"
miVariable="Estoy en principal"
funcionUno()
print(miVariable)
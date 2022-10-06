'''
def suma(a,b):
    return a+b
aliasSuma=suma
res=aliasSuma(5,6)
print(res)
'''
'''
suma=lambda a,b: a+b
res=suma(5,6)
print(res)
'''
'''
quitaEspacios=lambda texto: texto.replace(" ","")
res=quitaEspacios("Hola mundo")
print(res)
'''
'''
noParametros=lambda : 10+10
res=noParametros()
print(res)
'''
noParametrosnoRetorna=lambda : print("Hola mundo")
res=noParametrosnoRetorna()
print(res)

def noParametrosnoRetorna1():
    print("Hola mundo")
'''
for i in range(0,5):
    print(i)

def miRango(ini,fin):
    for i in range(ini,fin):
        if i%2==0:
            yield i*2,True
        else:
            yield i*2,False

for i in miRango(0,5):
    print(i)
'''
def comofuncionaGenerador():
    print("Hola")
    yield "Adios"
    print("Hola de nuevo")
    yield "Adios otra vez"
print(type(comofuncionaGenerador()))
res=list(comofuncionaGenerador())
print(res)
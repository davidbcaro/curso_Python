'''
#Que es la asignación simultánea de valores.
#a=5
#b=10
#c=15
a,b,c=10,15,20
print(f"a={a},b={b},c={c}")
'''
'''
#Funciones que retornan valores simultáneos.
def retornaValoresSimultaneos(a,b,c):
    return a+b,c
#d,f=retornaValoresSimultaneos(4,5,6)
#print(f"d={d},f={f}")
t=retornaValoresSimultaneos(4,5,6)
print(t)
print(f"t[0]={t[0]},t[1]={t[1]}")
'''
#Funciones que admiten indeterminada cantidad de valores.
def admiteIndeterminadaParametros(*args):
    suma = 0
    for i in args:
        print(f"{i}",end="+")
        suma = suma+i
    print(f"\nSuma={suma}")
admiteIndeterminadaParametros(4,5,6,7,8,9,10,11,12)
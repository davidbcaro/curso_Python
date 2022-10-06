'''
#continue
for letra in "Programador Novato":
    if letra==" ":
        continue
    print(letra,end="")
print()

var=10
while var>0:
    var=var-1
    if var==5:
        continue
    print(var)

#pass
for letra in "Programador Novato":
    if letra==" ":
        pass
    print(letra,end="")
print()

var=10
while var>0:
    var=var-1
    if var==5:
        pass
    print(var)

def funcionQueaunNoSeQueVaHacer():
    pass
funcionQueaunNoSeQueVaHacer()
'''
email=input("Ingresa un email:")
i=0
while i<len(email):
    if email[i]=="@":
        arroba=True
        break
    i=i+1
else:
    arroba=False
print("¿El correo tiene @?:",arroba)
'''
AND
0 0 = 0
1 0 = 0
0 1 = 0
1 1 = 1 

OR 
0 0 = 0
1 0 = 1
0 1 = 1
1 1 = 1 

NOT
0 = 1
1 = 0
'''
imc = 26
if imc > 19.9 or imc <= 25:
    print("Su peso es normal")

a = 10
b = 15
c = 20
resultado = ((a<b) and (b<c))
print(a<b , " and ", b<c," : ", resultado)
# True and True 
# resultado = True
resultado = ((a>b) and (b<c))
print(a>b, " and ", b<c," : ", resultado)
# Flase and True
# resultado = False
resultado = ((a>b) or (b<c))
print(a>b, " or ", b<c, " : ", resultado)
# False or True
# resultado = True
resultado_negado = not resultado
print("Not ", resultado,":", resultado_negado)
# resultado = False 
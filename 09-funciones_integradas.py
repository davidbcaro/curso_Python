'''
bin()
hex()
abs()
round()
pow()
'''
import math

valor = bin(10)
print("El número en binario es: ",valor)

valor = int('0b1010',2)
print("El número en entero es: ",valor)

valor = hex(10)
print('El número en hexadecimal es: ',valor)

valor = int('0xa',16)
print("El número entero es: ",valor)

valor = abs(-5)
print("El valor absoluto es: ",valor)

valor = round(6.6)
print("El número redondeado es: ",valor)

valor = pow(81, 0.5)
print("El valor de potencia es: ",valor)

# Librería math
valor = math.sqrt(2)
print("El valor de raíz cuadrada es: ",valor)

valor = math.pi
print("El valor de pi es: ", valor)




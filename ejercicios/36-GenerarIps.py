def decoradorPideBloques(generarIps):
    def antes():
        bloque1=int(input("Ingresa el bloque 1:"))
        bloque2=int(input("Ingresa el bloque 2:"))
        bloque3=int(input("Ingresa el bloque 3:"))
        ini=int(input("Ingresa el rango inicial del bloque 4:"))
        fin=int(input("Ingresa el rango final del bloque 4:"))
        return bloque1,bloque2,bloque3,ini,fin
    def despues(ips):
        for ip in ips:
            print(ip)
    def integrar(*args):
        bloque1,bloque2,bloque3,ini,fin=antes()
        ips=generarIps(bloque1,bloque2,bloque3,ini,fin)
        despues(ips)
    return integrar


@decoradorPideBloques
def generarIps(bloque1=0,bloque2=0,bloque3=0,ini=0,fin=0):
    for ip in range(ini,fin+1):
        yield str(bloque1)+"."+str(bloque2)+"."+str(bloque3)+"."+str(ip)

generarIps()

'''
for ip in generarIps(192,168,1,5,10):
    print(ip)
'''
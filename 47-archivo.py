#absoluta="C:\\Users\\eugenio\\Documents\\GitHub\\curso-python\\archivos\\hola.txt"
relativa="archivos\\hola.txt"
archivo=open(relativa,"r")
#print(archivo.read())
#print(archivo.readline())
#print(archivo.readline())
#print(archivo.readline())
#print(archivo.readlines())
#for linea in archivo.readlines():
#    print(linea)
#ESCRITURA
#relativa2="archivos\\hola2.txt"
#archivo2=open(relativa2,"w")
#archivo2.write("C#\nVB.NET\nASP.NET")
#ESCRITURA-LECTURA
relativa3="archivos\\hola3.txt"
archivo3=open(relativa3,"r+")
archivo3.write("Hola\nComo\nEstas")
archivo3.seek(0)
print(archivo3.read())
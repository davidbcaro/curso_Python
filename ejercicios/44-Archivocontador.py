'''
El programa creará un archivo llamado contador.txt que almacenará un contador de visitas
Si contador.txt no existe o está vacío lo crearemos con el número 0. Si existe simplemente leeremos el valor del contador.
Si se envía el argumento inc, se incrementará el contador en uno y se mostrará por pantalla.
Si se envía el argumento dec, se decrementará el contador en uno y se mostrará por pantalla.
Si no se envía ningún argumento, se mostrará el contado.

'''
import sys
fichero=open("contador.txt","a+")
fichero.seek(0)
contenido=fichero.readline()
if len(contenido)==0:
    contenido="0"
    fichero.write(contenido)
fichero.close()
try:
    contador=int(contenido)
    if len(sys.argv)==2:
        if sys.argv[1]=="inc":
            contador=contador+1
        elif sys.argv[1]=="dec":
            contador=contador-1
    print(contador)
    fichero=open("contador.txt","w")
    fichero.write(str(contador))
    fichero.close()
except:
    print("Error en archivo")

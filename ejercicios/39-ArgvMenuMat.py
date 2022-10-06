import sys
if __name__=="__main__":
    tam=len(sys.argv)
    for argumento in sys.argv:
        if argumento=="-h" or argumento=="--help" or argumento=="" :
            print("Bienvenido al programa\
\n-h or --help: Ayuda\
\n-s or --suma: Sumar n cantidad de numeros\
\n-r or --resta: Restr n cantidad de numeros\
\n-m or --mul: Multiplicar n cantidad de numeros\
\n-d or --div: Dividir n cantidad de numeros")
        if argumento=="-s" or argumento=="--suma":
            i=2
            if tam>3:
                res=0
                while i<tam:
                    res=res+int(sys.argv[i])
                    i=i+1
                print("Resultado=",res)
            else:
                print("Faltan argumentos")
        if argumento=="-r" or argumento=="--resta":
            i=2
            if tam>3:
                res=0
                while i<tam:
                    if i==2:
                        res=int(sys.argv[i])
                    else:
                        res=res-int(sys.argv[i])
                    i=i+1
                print("Resultado=",res)
            else:
                print("Faltan argumentos")
        if argumento=="-m" or argumento=="--mul":
            i=2
            if tam>3:
                res=1
                while i<tam:
                    res=res*int(sys.argv[i])
                    i=i+1
                print("Resultado=",res)
            else:
                print("Faltan argumentos")
        if argumento=="-d" or argumento=="--div":
            i=2
            if tam>3:
                res=0
                while i<tam:
                    if i==2:
                        res=int(sys.argv[i])
                    else:
                        res=res/int(sys.argv[i])
                    i=i+1
                print("Resultado=",res)
            else:
                print("Faltan argumentos")


#python programa.py -s 1 2 3
import sys
if __name__=="__main__":
    for argumentos in sys.argv:
        if argumentos=="-h" or  argumentos=="--help" :
            print("Bienvenido al programa x\
\n-s:sumar\
\n-r:restas")
        #print(argumentos)
    #print(sys.argv)
def A(parametro=True):
    def _A(B):
        def antes():
            print("************")
        def despues():
            print("************")
        def C(*args):
            if parametro==True:
                antes()
            res=B(*args)
            if parametro==True:
                despues()
            return res
        return C
    return _A

@A(True)
def B(a,b):
    print(f"Hola mundo a={a} b={b}")
    return a+b

res=B(5,6)
print(res)

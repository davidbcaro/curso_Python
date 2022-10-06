'''
El diccionario tendrá una lista con 3 empleados con nombre y edad. 
El mismo diccionario tendrá una lista de 3 de autos con marca, modelo 
    y también cada auto tendrá 2 submodelos
Accederemos a la edad del empleado número 3.
Accederemos al segundo submodelo del auto número 2.
'''
empresa={
'empleados':[
    {'nombre':'Maria','edad':20},
    {'nombre':'Esteban','edad':30},
    {'nombre':'Pepe','edad':25}
],
'autos':[
    {'marca':'Ford','modelo':'f20','submodelos':['f20.01','f20.02']},
    {'marca':'Nissan','modelo':'n20','submodelos':['n20.01','n20.02']},
    {'marca':'Seat','modelo':'s20','submodelos':['s20.01','s20.02']}
]
}
print("empresa['empleados'][2]['edad']=",empresa['empleados'][2]['edad'])
print("empresa['autos'][2]['submodelos'][1]=",empresa['autos'][2]['submodelos'][1])
print(empresa)
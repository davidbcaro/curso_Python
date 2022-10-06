diccionario = {
    1: "Python",
    2: "Java",
    3: "Javascript",
    4: (1, 3)
}
print(diccionario)
print('len(diccionario)=', len(diccionario))
print("diccionario['Python']=", diccionario[3])
print(diccionario)

print("diccionario['c++']=4=", diccionario)
diccionario[5] = "C++"
print("diccionario['c++']=5=", diccionario)
# del(diccionario['c++'])
# print("del(diccionario['c++'])=", diccionario)
# diccionario['c/c++'] = [4,5]
# print("diccionario['c/c++']=[4,5]=", diccionario)
# #diccionario['c/c++'] = (4,5)
# #print("diccionario['c/c++']=(4,5)=", diccionario)
# diccionario['otros'] = {100,101,102}
# print("diccionario['otros']={100,101,102}=", diccionario)

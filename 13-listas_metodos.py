lista = [1, 1, 2, 3]
#lista[0] = "Enero"
print(lista)
print("len(lista)=", len(lista))
lista.append(4)
print("list.append(4)=", lista)
lista.insert(0,0)
print("list.insert(0,0)=", lista)
lista.extend([5, 6, 7])
print("list.extend([5,6,7])=", lista) # [0, 1, 1, 2, 3, 4, 5, 6, 7]
lista += [8,9,10]
print("list+=[8,9,10]=", lista)
num = 5
if num in lista:
    print(f"El numero {num} si esta en la lista")
else:
    print(f"El numero {num} no esta en la lista")
print("lista.index(5)=", lista.index(5))
print("lista.count(1)=", lista.count(1))
i = 3
lista.pop(i)
print("lista.pop(0)=", lista)
lista.remove(5)
print("lista.remove(5)=", lista)
lista.reverse()
print("lista.reverse()=", lista)
lista.sort()
print("lista.sort()=", lista)
lista.clear()
print("lista.clear()=", lista)
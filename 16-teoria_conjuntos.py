a = {1, 2, 3, 4}
b = {4, 5, 6, 7}
d = {1, 2, 3, 4, 5, 6}
e = {11, 12, 13, 14, 15, 16}
print("a==b:", a==b)
c = a|b
print("c=a|b=", c)
c = a&b
print("c=a&b=", c)
c = a-b
print("c=a-b=", c)
c = a^b
print("c=a^b=", c)
print("a.issubset(d)=", a.issubset(d))
print("d.issubset(a)=", d.issubset(a))
print("d.issubset(a)=", d.issuperset(a))
print("a.isdisjoint(e)=", a.isdisjoint(e))
f = frozenset({1, 2, 3})
#f.add(2)
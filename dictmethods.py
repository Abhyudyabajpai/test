d = dict(a =1,b=2,c=3,d=4)
print(d)
print("using copy: ")
c = d.copy()
print(c)
print("using fromkeys: ")
a = {}.fromkeys(['name','score','id'],'unknown')
print(a)

print("get keyword: ")
print(a.get('name'))

print("clear keyword")
d.clear()
print(d)
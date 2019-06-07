x = dict(a= 1,b=2,c=3,d=4)
y = dict(e=5)

print("using pop keyword: ")
x.pop('b')       #takes 1 arguement
print(x)

print("using popitem:")
x.popitem()    #takes no arguement
print(x)

print("using update keyword:")
y.update(x)
print(y)      #adds x to y 
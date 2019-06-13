def count(max):
    c = 1
    while c <= max:
        yield c
        c +=1

a = count(5)
for n in a:
    print(n)

print(type(a))
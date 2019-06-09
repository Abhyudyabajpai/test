def sum(*args):
    t = 0
    for a in args:
        t += a
    return t 

print(sum(1,5,9,2))
print(sum(3,7))

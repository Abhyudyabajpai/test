#Passing func as args
def sum(n,fn):
    t = 0
    for num in range(n):
        t += fn(num)
    return t

def sqr(x):
    return x*x

print(sum(3,sqr))

#it prints the sum of sqr of 0,1,2 i.e 0+1+4 = 5






















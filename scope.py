#global scope
name = 'bale'
def say():
    return f"hello {name}"

print(say())
print(name)
#local scope
def sayhi():
    sr = 'morris'
    return f"hello {sr}"
print(sayhi())

from functools import wraps

def ensure_first_arg(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args,**kwargs):
            if args and args[0] != val:
                return f"First value needs to be {val}"
            return fn(*args,**kwargs)
        return wrapper
    return inner

@ ensure_first_arg("blue")
def color(*c):
    print(c)

print(color("blue","red"))
print(color("green","blue"))
from functools import wraps
 
def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if len(args) < 3:
            return fn(*args, **kwargs)
        return "Too many arguments!"
    return wrapper

    @ensure_fewer_than_three_args
    def add(*nums):
         return sum(nums)
    
    add(6,7)
    add(1,2,3)
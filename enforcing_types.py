def enforce(*types):
    def decorator(f):
        def new_func(*args,**kwargs):
            newargs =[]
            for(a,t) in zip(args,types):
                newargs.append( t(a))
            return f(*newargs,**kwargs)
        return new_func
    return decorator

@enforce(str,int)
def en(msg,times):
    for time in range(times):
        print(msg)

en("hello",4)
en("Ceil",'5')
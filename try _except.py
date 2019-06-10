def get(d,key):
    try:
        print(d[key])
    except KeyError:
        print("not_found")
    else:
        print( "this runs when try is true")
    finally:
        print( "this will run no matter what")
        

d= {"name":"gale"}
print(get(d,"asd"))

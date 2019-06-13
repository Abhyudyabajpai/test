def be_polite(fn):
    def wrapper():
        print("Pleasure to meet you")
        fn()
        print("Have a great day!")
    return wrapper

def greet():
    print("My name is Charlie")
    
c = be_polite(greet)   #decorating the function
c()
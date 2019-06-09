def greetings(**kwargs):
    for k,v in kwargs.items():
        print(f"welcome: {k} {v}")

greetings(Trent ='Bolt',John ='Miller')

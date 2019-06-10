def color(name,colour):
    if type(name) is not str:
        raise TypeError("only strings allowed")
    print(f"{name} likes {colour}")

color("alley","green")
color(21,"red")
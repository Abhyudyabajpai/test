def divide(a,b):
    try:
        r = a/b
    except (ZeroDivisionError,TypeError) as err:
        print("wrong input")
    else:
        print(f"{a} divided by {b} is {r}")

divide(1,5)
divide(1,0)

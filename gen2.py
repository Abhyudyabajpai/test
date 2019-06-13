def curent_beat():
    n =(1,2,3,4)
    i = 0
    while True:
        if i >= len(n): 
            i =0
            yield n[i]
            i += 1
